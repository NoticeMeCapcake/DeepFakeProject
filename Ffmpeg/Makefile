#файл для быстрой сборки и запуска контейнеров (нужно подправить скрипт, чтобы у него была фиксирована папка)
#папка tmp будет лежать там же, где питоновский скрипт и исходники (resources)

WAY = "$(HOME)/data/tmp"
build:
	docker build -t ffmpeg_scripts .
video_to_images:
	docker run -v $(WAY)/video:/data/video -v buffer_vol:/data --rm ffmpeg_scripts ./video_to_images.sh
images_to_video:
	docker run -v $(WAY)/video:/data/video -v buffer_vol:/data --rm ffmpeg_scripts ./images_to_video.sh
#outtmp связан с папкой result
video_to_audio:
	docker run -v $(WAY)/video:/data/video -v buffer_vol:/data --rm ffmpeg_scripts ./video_to_audio.sh
video_and_audio:
	docker run -v $(WAY)/video:/data/video -v buffer_vol:/data --rm ffmpeg_scripts ./video_add_audio.sh