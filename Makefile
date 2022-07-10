build_all:
	docker build -t ubunta-img ./ubuntudocker
	docker build -t gpen-img ./GPEN
	docker build -t ffmpeg_scripts ./Ffmpeg
run_prev:
	docker run -v $(HOME)/data/temp/image:/data/images -v buffer_vol:/data --rm gpen-img ./Proc.sh
run_proc:
	cd ./SimSwap
	make swap
	cd ..
run_post:
	docker run -v $(HOME)/data/temp/video:/data/video -v buffer_vol:/data --rm ffmpeg_scripts ./video_to_audio.sh
	docker run -v $(HOME)/data/temp/video:/data/video -v buffer_vol:/data --rm ffmpeg_scripts ./video_to_images.sh
	docker run -v buffer_vol:/data --rm gpen-img ./Proc.sh
	docker run -v $(HOME)/data/temp/video:/data/video -v buffer_vol:/data --rm ffmpeg_scripts ./images_to_video.sh
	docker run -v $(HOME)/data/temp/video:/data/video -v buffer_vol:/data --rm ffmpeg_scripts ./video_add_audio.sh
