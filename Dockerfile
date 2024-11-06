FROM python:3.9-slim

LABEL authors="chauke"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV=development

CMD ["python", "main.py"]

