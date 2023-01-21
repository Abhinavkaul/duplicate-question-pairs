PROJECT=duplicate-question-pair

local-tests:
	docker build -t test .
	docker run test