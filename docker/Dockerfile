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
# COPY python-sample-vscode-django-tutorial .

RUN git clone https://github.com/tokibito/django-example-todo.git . && \
    pip install -r requirements.txt && \
    pip install -r requirements-extras.txt && \
    cd myproject && \
    python manage.py migrate && \
    python manage.py createsuperuser



WORKDIR /app/myproject

CMD ["python", "manage.py",  "runserver", "0.0.0.0", "8000"]

# RUN add-apt-repository ppa:jonathonf/python-3.6
# RUN apt-get update
# RUN apt-get install -y python3.6 python3.6-dev python3-pip
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 0

# RUN python -m pip install pip --upgrade
# RUN python -m pip install wheel

# # RUN pip install torch torchvision
# RUN pip install -U git+https://github.com/catalyst-team/catalyst

# RUN pip install -U git+https://github.com/qubvel/segmentation_models.pytorch
# RUN pip install --upgrade --force-reinstall https://download.pytorch.org/whl/cu100/torchvision-0.4.0-cp36-cp36m-manylinux1_x86_64.whl

# RUN pip install -U git+https://github.com/albu/albumentations


# RUN pip install jupyterlab
# RUN pip install jpeg4py
# RUN pip install pytorch_toolbelt
# RUN pip install mlcomp
# WORKDIR /tmp
# RUN git clone https://github.com/NVIDIA/apex
# WORKDIR apex
# RUN pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./
# ENV PYTHONPATH "${PYTHONPATH}:/project"
# # ENV TORCH_MODEL_ZOO="/data/pretrainedmodels"
# ENV TORCH_HOME="/data/pretrainedmodels"
