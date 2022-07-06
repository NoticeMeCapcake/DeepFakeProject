#!/bin/bash

# На вход командной строки: полное имя файла с видео в формате mp4
# После работы создастся папка data/audio, где будет лежать аудио в формате mp3

#create dir for new audio
name_data_dir=`pwd`
name_data_dir+="/data/audio/"

if [ ! -d $name_data_dir ]; then
    mkdir -p $name_data_dir;
fi

#check exist file with video
if [ ! -f $1 ]; then
    echo "File not found!"
    exit 1
fi

#make new file name for audio
name_file_without_ext=$(basename -- "$1")
name_file_without_ext="${name_file_without_ext%.*}"
name_audio=$name_data_dir
name_audio+=$name_file_without_ext
name_audio+=".mp3"

#get audio with mp3 from video
ffmpeg -i $1 -vn -ar 44100 -ac 2 -ab 192k -f mp3 $name_audio