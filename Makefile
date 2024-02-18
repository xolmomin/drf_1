build:
	docker build -t harry-p17group:latest .
	docker run -p 8000:8000 harry-p17group:latest

mig:
	python3 manage.py makemigrations && python3 manage.py migrate

check:
	isort .
	flake8 .