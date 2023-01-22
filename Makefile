PROJECT=duplicate-question-pair

build-image:
	docker build -t test .



user-input: build-image
	docker run -it test /bin/bash -c "cd tests && python run.py"

docker-compose:
	docker-compose up
	docker-compose down