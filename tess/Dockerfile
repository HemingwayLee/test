FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y build-essential software-properties-common \
    wget dpkg bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 \
    libxrender1 libgl1-mesa-glx git mercurial make xz-utils file \
    language-pack-ja-base language-pack-ja fonts-noto-cjk fonts-takao \ 
    fonts-vlgothic fonts-ipafont

RUN /bin/bash -c "echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >> ~/.bashrc"
RUN /bin/bash -c "source ~/.bashrc"
RUN locale-gen ja_JP.UTF-8

ENV LANG=C.UTF-8 LC_ALL=ja_JP.UTF-8
# ENV LD_LIBRARY_PATH "$LD_LIBRARY_PATH:/usr/local/lib"

# RUN add-apt-repository ppa:alex-p/tesseract-ocr -y && \
#     apt-get update && apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev

RUN add-apt-repository ppa:alex-p/tesseract-ocr -y && \
    apt-get update && apt-get install -y tesseract-ocr-all 

RUN wget https://repo.continuum.io/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh -O ~/miniconda.sh
RUN /bin/bash ~/miniconda.sh -b -p /opt/conda 
RUN rm ~/miniconda.sh
RUN /opt/conda/bin/conda clean -tipsy
RUN ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
RUN echo "conda activate base" >> ~/.bashrc
RUN /opt/conda/bin/conda update -n base -c default conda

WORKDIR /root
ARG conda_env=mypy
COPY environment.yaml ./
RUN /opt/conda/bin/conda env create -v -f environment.yaml
RUN echo "conda activate $conda_env" >> ~/.bashrc
ENV PATH /opt/conda/envs/$conda_env/bin:$PATH
ENV CONDA_DEFAULT_ENV $conda_env

RUN apt-get autoremove -y && apt-get clean

# COPY tests /root/tests
# COPY models /root/models
# COPY training_data /root/training_data
# COPY testing_data /root/testing_data
# COPY output /root/output

COPY src /root/src
WORKDIR /root/src
