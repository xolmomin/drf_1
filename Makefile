build:
	docker build -t harry-p17group:latest .
	docker run -p 8000:8000 harry-p17group:latest