# Docker Workshop

## Installation and Minimal Example

Run hello-world:
```sh
$ docker run -it --rm hello-world
```

## What is a Dockerfile? What is a Docker image? What is a Docker Container?

![](https://phoenixnap.com/kb/wp-content/uploads/2019/10/crating-a-docker-container.png)

Save image from within docker container:

```sh
$ docker commit <container_id> <new_docker_image_tag>
```

## Differents between a VM and a (Docker) Container. Pros and Cons?

![](https://blog.netapp.com/wp-content/uploads/2016/03/Screen-Shot-2018-03-20-at-9.24.09-AM-935x500.png)

## Creating own Docker image. Best practises

```sh
$  git clone https://github.com/encode/starlette-example.git
```

Build the image:

```sh
$ docker build -t $(whoami)/example-app-2 -f ./docker/Dockerfile .

# it builds image as latest one
# you can write specific version at the end of image name after colon (fistbook/pentagram:10.0.1-devel)
```

## Running Docker Container

Run the container:

```sh
$ docker run \
  --name example_app_2 \
  -p 8000:8000 \
  -it --rm \
  $(whoami)/example-app-2:latest bash
```

## Volumes and Mounts

```sh
$ docker volume create datavolume1
```

```sh
$ docker run ... -v datavolume1:/data ...

# or using a bindmount:
$ docker run ... -v /path/data:/data                         # or
$ docker run ... --mount type=bind,source=/path/data,target=/data
```

## Networks

```sh
$ docker network create mynet

$ docker run ... --network mynet --name alpine1 alpine:latest ash
$ docker run ... --network mynet --name alpine2 alpine ash

```

```sh
$ docker container attach alpine1

# ping -c 2 alpine 2
```

## Docker Compose vs. Docker Swarm

These are different things!
 
Docker Compose - high-level API for Docker Engine.
Docker Swarm - the orchestration tool.

## Useful Resources

1. [Docker Overview](https://docs.docker.com/get-started/overview/)

1. [Install Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

1. [Docker Python API](https://docker-py.readthedocs.io/en/stable/)

1. [Katacoda](https://www.katacoda.com/learn)
