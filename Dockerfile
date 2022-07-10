FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install build-essential
RUN apt-get -y install libgl1-mesa-glx
RUN apt-get -y install python3
RUN apt-get -y install pip
RUN apt-get -y install build-essential cmake git pkg-config
RUN apt-get -y install libjpeg8-dev libtiff-dev libpng-dev
RUN apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
RUN apt-get -y install libgtk2.0-dev
RUN apt-get -y install libatlas-base-dev gfortran

RUN python3 -m pip install --upgrade pip
RUN pip install opencv-python
RUN pip install matplotlib
RUN pip install scikit-image
RUN pip install numpy
RUN pip install torch
RUN pip install timm
