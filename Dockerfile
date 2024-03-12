FROM python:3.11-slim

WORKDIR /app
RUN apt update && apt install -y libjpeg-dev zlib1g zlib1g-dev
COPY requirements.txt ./
RUN pip install -r requirements.txt \
    && rm requirements.txt
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8457
ENTRYPOINT ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8457"]
