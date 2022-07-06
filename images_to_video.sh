#!/bin/bash

# На вход: директория, где лежат images(кадры) по порядку, начиная с 1, \
# и выходной файл, в который будет записан результат (-d directory/(на конце обязателен слеш) -o output_file)
# После работы создастся папка data/video, где будет видео с именем переданным в командной строке

#check keys
if [ "$#" -eq 0 ]; then
    echo "Invalid arguments! Need keys with arguments: -d directory with images -o output file.mp4"
    exit 1
fi

#get directory and output file from keys
while [ -n "$1" ]
do
case "$1" in
    -d) name_directory_with_images=$2
        shift;;
    -o) name_video_file=$2
        shift;;
    --) shift
break ;;
*) echo "$1 is not an option";;
esac
shift
done

#check directory from parametres is empty 
if [ `ls $name_directory_with_images | wc -l` -eq 0 ]; then
    echo "Empty directory"
    exit 1
fi

#check format of output file 
if [[ $name_video_file != *.mp4 ]]; then
    echo "Invalid format for output file.(Format is mp4)"
    exit 1
fi

#create dir for new video
name_data_dir=`pwd`
name_data_dir+="/data/video/"

if [ ! -d $name_data_dir ]; then
    mkdir -p $name_data_dir;
fi

#get images name with path 
path_to_images=$name_directory_with_images
path_to_images+="image%d.jpg"

#make new file name for video with path
name_data_dir+=$(basename -- "$name_video_file")

ffmpeg -start_number 1 -f image2 -i $path_to_images $name_data_dir