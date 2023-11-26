FROM python:3.11-slim

RUN pip install poetry==1.3.2
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-cache --no-root --no-interaction \
    && rm pyproject.toml poetry.lock
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8457
ENTRYPOINT ["poetry", "run", "gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8457"]
