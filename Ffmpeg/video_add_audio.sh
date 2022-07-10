#!/bin/bash

# На вход: -v полное имя файла с видео.mp4 -a полное имя файла с аудио.mp3
# После работы создастся папка data/video_with_audio, где будет видео со звуком

#get audio and vidoe dir from keys

#check exist file
name_audio_file="./data/audio/audio.mp3"
name_video_file="./data/video/res.mp4"
if [ ! -f $name_audio_file ] && [ ! -f $name_video_file ]; then
    echo "This file(s) is not exist"
    exit 1
fi

#create dir for new video
name_data_dir="./data/video/vid_aud.mp4"

#create new file name with video and audio

ffmpeg -i $name_audio_file -i $name_video_file $name_data_dir
