FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    git \
    software-properties-common \
    python3-dev \
    python3-pip

RUN ln -s python3 /usr/bin/python
RUN ln -s pip3 /usr/bin/pip


WORKDIR /app
# COPY starlette-example .

RUN git clone https://github.com/encode/starlette-example.git . && \
    pip install -r requirements.txt

CMD ["python", "app.py"]
