FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt \
    && rm requirements.txt
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8457
ENTRYPOINT ["poetry", "run", "gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8457"]
