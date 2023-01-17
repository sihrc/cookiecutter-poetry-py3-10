FROM python:3.10-alpine AS poetry-builder

ARG POETRY_INSTALL_ARGS
ENV ENV="/root/.ashrc"
ENV PATH=/root/.local/bin:/root/.cargo/bin:${PATH}

RUN apk update && \
    apk add --no-cache curl && \
    curl -sSL https://install.python-poetry.org/ | python3 && \
    poetry config virtualenvs.in-project true


WORKDIR /app
ADD pyproject.toml /app/

RUN poetry install

# Start Project Dockerfile
FROM alpine:3.15

LABEL version="{{cookiecutter.version}}"
LABEL author="{{cookiecutter.author}}"
LABEL email="{{cookiecutter.email}}"
LABEL description="{{cookiecutter.project_description}}"

ENV PATH = "/app/.venv/bin:${PATH}"
ENV PYTHONPATH="/app/.venv/lib/python3.10/site-packages:/{{ cookiecutter.project_slug }}"

RUN apk add --no-cache vim bash

COPY --from=poetry-builder /app /app
RUN ln -sf $(which python3) /venv/.venv/bin/python

WORKDIR /{{ cookiecutter.project_slug }}
COPY . /{{ cookiecutter.project_slug }}

ENTRYPOINT [ "bash" ]
