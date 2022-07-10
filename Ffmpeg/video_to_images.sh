#!/bin/bash

# На вход: полное имя файла с видео
# После работы создастся папка data/images/file_video_name, где будут лежать кадры

#check exist file with video
path_video="./data/video/video.mp4"
if [ ! -f $path_video ]; then
    echo "File not found!"
    exit 1
fi

#create dir for new images
#name_data_dir=`pwd`
name_data_dir+="./data/images/"
#name_data_dir+=$name_file_without_ext

if [ ! -d $name_data_dir ]; then
    mkdir -p $name_data_dir;
fi

#create images name with path 
path_to_images=$name_data_dir
path_to_images+="image%d.jpg"

#get images.jpg from video
ffmpeg -i $path_video $path_to_images