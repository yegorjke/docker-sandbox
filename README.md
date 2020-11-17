# Docker Workshop

## Part 1

1. Installation and Minimal Example


2. What is a Dockerfile? What is a Docker image? What is a Docker Container?

Докерфайл - это "исходный код" докер контейнера. В нем описывается шаблон того, как будет построен контейнер.
Докер образ - это готовый шаблон, из которого можно запустить контейнер.
Контейнер создается из образа и содержит в себе абсолютно все, что описано в докерфайле.

Подводный камень:
Если контейнер зависит от содержимого проекта (код или т. п.), то образ нужно заново сбилдить, иначе изменения не подтянутся внутрь контейнера.
Сделать пример и запустить без билда.

3. Differents between a VM and a (Docker) Container. Pros and Cons?

![](https://blog.netapp.com/wp-content/uploads/2016/03/Screen-Shot-2018-03-20-at-9.24.09-AM-935x500.png)

4. Creating own Docker image

```sh
$ git clone https://github.com/tokibito/django-example-todo.git
```

Build the image:

```sh
$ docker build \
  -t $(whoami)/ubuntu_custom_image \
  -f ./docker/Dockerfile \
  --build-arg version="18.04" \
  .

# it builds image as latest one
# you can write specific version at the end of image name after colon (fistbook/pentagram:10.0.1-devel)
```


5. Running Docker Container

Run the container:

```sh
$ docker run \
  --shm-size 8G \
  -p $ARG2:$ARG2 \
  --volume=$XSOCK:$XSOCK:rw \
  --mount type=bind,source="$PWD",target=/app \
  -it --rm \
  --name my_custom_container \
  $(whoami)/ubuntu_custom_image:latest bash
```

## Part 2

6.


7.


8. Docker Compose (vs.) Docker Swarm


9. Working with Vagrant


## Useful Resources

[Docker Python API](https://docker-py.readthedocs.io/en/stable/)
