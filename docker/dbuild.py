#!/usr/bin/env python
import argparse
from functools import reduce
import getpass
import os
import re
import subprocess
import sys
import tempfile


def fullTag(tag):
    """
    Args:
        tag: string in format '[<user>/]<tag>[:<version>]'

    Returns:
        string in format '<user>/<tag>:<version>'

    Raises:
        ValueError
    """
    match = re.match(r"^(?:([\w]{0,64})\/)?([\w][\w.-]{0,64})" r"(?::([\w.-]{1,32}))?$", args.tag)

    if not match:
        raise NameError(f"'{args.tag}' is not a valid image tag, should be " "'[<user>/]<name>[:<version>]'")

    user, tag, version = match.groups()
    user = user or getpass.getuser()
    version = version or "latest"
    return f"{user}/{tag}:{version}"


def userLayers(tag):
    """
    Build layer that adds a user to image

    Args:
        tag: source image tag

    Returns: list of strings
    """
    # empty line in case original Dockerfile not ends with line break
    result = [f"FROM {tag}"]
    result.extend(["ARG user_name", "ARG user_id", "ARG group_id"])
    # create user with home directory, add it to sudo group
    # install sudo package and allow password-less sudo
    result.append(
        "RUN groupadd -g $group_id $user_name && "
        "useradd -mu $user_id -g $group_id -s /bin/bash $user_name && "
        "usermod -aG sudo $user_name && "
        "apt-get update && apt-get install -y sudo && "
        'echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers'
    )
    # login to container as <user> and set working directory to $HOME
    result.extend(["USER $user_name", 'WORKDIR "/home/$user_name"'])
    return "\n".join(result)


def buildArgs(args):
    """
    Args:
        args: list of strings in format ["<key>=<value>", ...]

    Returns:
        list of strings in format ["--build-arg", "<key>=<value>", ...]

    Raises:
        ValueError
    """
    if not args:
        return []

    for arg in args:
        if not re.match(r"^[^=]+=[^=]+$", arg):
            raise ValueError(f"'{arg}' is not a valid build argument")

    return reduce(lambda x, y: x + ["--build-arg", y], args, [])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build docker image")
    parser.add_argument("-t", "--tag", type=str, help="Docker image tag (name)", required=True)
    parser.add_argument(
        "-f", "--file", type=str, default="Dockerfile", help="docker file name ('Dockerfile' is default)"
    )
    parser.add_argument(
        "-p", "--path", type=str, default=".", help="Path to docker context used by COPY. " "('.' is default)"
    )
    parser.add_argument(
        "--build-arg", type=str, action="append", help="Builld arguments passed to docker: " "'<key>=<value>'"
    )
    parser.add_argument("--root", action="store_true", help="Build image without adding current user")
    args = parser.parse_args()

    imageTag = fullTag(args.tag)

    command = ["docker", "build"]
    command.extend(["-t", imageTag])
    command.extend(buildArgs(args.build_arg))

    if not os.path.isfile(args.file):
        raise IOError(f"'{args.file}': file not found")

    command.extend(["-f", args.file])

    if not os.path.isdir(args.path):
        raise OSError(f"'{args.path}' is not a directory")

    command.append(args.path)

    # run docker build
    error = subprocess.call(command)
    if error != 0:
        exit(error)

    if not args.root:
        command = ["docker", "build", "-t", imageTag]
        command.extend(["--build-arg", f"user_name={getpass.getuser()}"])
        command.extend(["--build-arg", f"user_id={os.getuid()}"])
        command.extend(["--build-arg", f"group_id={os.getgid()}"])

        # tell docker to read Dockerfile from stdin
        command.append("-")
        # layers for running container with current user
        with tempfile.TemporaryFile(mode="w") as dockerfile:
            # write user layers to temp file
            dockerfile.writelines(userLayers(imageTag))
            # flush file buffer
            dockerfile.flush()
            # go to file beginning
            dockerfile.seek(0)
            # pipe temporary file to stdin
            os.dup2(dockerfile.fileno(), sys.stdin.fileno())

    os.execvp(command[0], command)
