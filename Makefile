PROJECT=duplicate-question-pair

build-image:
	docker build -t test .

pytest: build-image
	docker run -it test /bin/bash -c "cd tests && pytest test_model.py"

user-input: build-image
	docker run -it test /bin/bash -c "cd tests && python run.py"

docker-compose:
	docker-compose up
	docker-compose down