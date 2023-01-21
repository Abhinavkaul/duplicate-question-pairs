PROJECT=duplicate-question-pair

local-tests:
	docker build -t test .
	docker run test

docker-compose:
	docker-compose up
	docker-compose down