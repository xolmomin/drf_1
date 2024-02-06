FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0:8000"]


# docker build -t harry-p17group:latest .
# docker run --name p17_gruppa_container -p 8000:8000 harry-p17group:latest