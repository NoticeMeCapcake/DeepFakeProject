FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

COPY . .
RUN chmod 777 video_to_images.sh
RUN chmod 777 images_to_video.sh
RUN chmod 777 video_add_audio.sh
RUN chmod 777 video_to_audio.sh
