#!/bin/bash

# На вход: полное имя файла с видео
# После работы создастся папка data/images/file_video_name, где будут лежать кадры

#check exist file with video
if [ ! -f $1 ]; then
    echo "File not found!"
    exit 1
fi

name_file_without_ext=$(basename -- "$1")
name_file_without_ext="${name_file_without_ext%.*}/"

#create dir for new images
name_data_dir=`pwd`
name_data_dir+="/data/images/"
name_data_dir+=$name_file_without_ext

if [ ! -d $name_data_dir ]; then
    mkdir -p $name_data_dir;
fi

#create images name with path 
path_to_images=$name_data_dir
path_to_images+="image%d.jpg"

#get images.jpg from video
ffmpeg -i $1 $path_to_images