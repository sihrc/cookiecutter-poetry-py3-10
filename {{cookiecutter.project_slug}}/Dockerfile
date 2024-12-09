FROM python:3.12.6 AS builder

ENV PATH="/root/.local/bin:${PATH}"

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry self update \
    && poetry config virtualenvs.in-project true


COPY pyproject.toml poetry.lock /venv/

WORKDIR /venv/

RUN poetry install

FROM python:3.12.6

LABEL version="{{cookiecutter.version}}"
LABEL author="{{cookiecutter.author}}"
LABEL email="{{cookiecutter.email}}"
LABEL description="{{cookiecutter.project_description}}"

ENV PYTHONPATH=/{{cookiecutter.project_slug}} PATH=/venv/.venv/bin:/{{cookiecutter.project_slug}}/bin:${PATH}
COPY --from=builder /venv /venv

RUN apt update \
    && apt upgrade -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /{{ cookiecutter.project_slug }}
COPY . /{{ cookiecutter.project_slug }}


ENTRYPOINT [ "bash" ]
