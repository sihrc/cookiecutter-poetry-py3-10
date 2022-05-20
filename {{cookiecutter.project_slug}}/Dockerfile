FROM python:3.10-alpine AS poetry-builder

ARG POETRY_INSTALL_ARGS
ENV ENV="/root/.ashrc"
ENV PATH=/root/.local/bin:/root/.cargo/bin:${PATH}

RUN apk update && \
    apk add --no-cache \
    curl \
    gcc \
    g++ \
    libressl-dev \
    musl-dev \
    git \
    libffi-dev && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile=minimal && \
    curl -sSL https://install.python-poetry.org/ | python3 && \
    poetry config virtualenvs.in-project true {% if cookiecutter.use_private_repos == "y" %} && \
    apk add --no-cache openssh && \
    mkdir -p -m 0600 ~/.ssh && ssh-keyscan github.com >> ~/.ssh/known_hosts {% endif %}


WORKDIR /app
ADD pyproject.toml /app/

RUN {% if cookiecutter.use_private_repos == "y" %} --mount=type=ssh {% endif %} poetry install --no-ansi ${POETRY_INSTALL_ARGS}

# Start Project Dockerfile
FROM alpine:3.15

LABEL version="{{cookiecutter.version}}"
LABEL author="{{cookiecutter.author}}"
LABEL email="{{cookiecutter.email}}"
LABEL description="{{cookiecutter.project_description}}"

ENV PATH = "/app/.venv/bin":${PATH}

COPY --from=poetry-builder /app /app

WORKDIR /{{ cookiecutter.project_slug }}
COPY . /{{ cookiecutter.project_slug }}
