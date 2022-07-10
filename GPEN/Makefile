build:
	docker build -t gpen_img .

post:
	docker run -v buffer_vol:/data --rm gpen_img
prep:
	docker run -v $(HOME)/results:/results/outs-bfr -v buffer_vol:/data --rm gpen_img
