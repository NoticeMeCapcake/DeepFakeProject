#!/bin/bash

# На вход: -v полное имя файла с видео.mp4 -a полное имя файла с аудио.mp3
# После работы создастся папка data/video_with_audio, где будет видео со звуком

#check keys
if [ "$#" -eq 0 ]; then
    echo "Invalid arguments! Need keys with arguments: -v video -a audio"
    exit 1
fi

#get audio and vidoe dir from keys
while [ -n "$1" ]
do
case "$1" in
    -a) name_audio_file=$2
        shift;;
    -v) name_video_file=$2
        shift;;
    --) shift
break ;;
*) echo "$1 is not an option";;
esac
shift
done

#check exist file
if [ ! -f $name_audio_file ] && [ ! -f $name_video_file ]; then
    echo "This file(s) is not exist"
    exit 1
fi

#create dir for new video
name_data_dir=`pwd`
name_data_dir+="/data/video_with_audio/"

if [ ! -d $name_data_dir ]; then
    mkdir -p $name_data_dir;
fi

#create new file name with video and audio
name_file_without_path=$(basename -- "$name_video_file")
name_data_dir+=$name_file_without_path

ffmpeg -i $name_audio_file -i $name_video_file $name_data_dir
