#!/bin/bash

# На вход: директория, где лежат images(кадры) по порядку, начиная с 1
# После работы создастся папка data/video, где будет видео

#create dir for new video
name_data_dir="./data/video/"

if [ ! -d $name_data_dir ]; then
    mkdir -p $name_data_dir;
fi

path_to_images="./data/images/"

#check directory from parametres is empty 
if [ `ls $path_to_images | wc -l` -eq 0 ]; then
    echo "Empty directory"
    exit 1
fi

#get images name with path 

path_to_images+="image%d.jpg"

#make new file name for video with path
name_data_dir+="res.mp4"

ffmpeg -start_number 0 -f image2 -i $path_to_images $name_data_dir