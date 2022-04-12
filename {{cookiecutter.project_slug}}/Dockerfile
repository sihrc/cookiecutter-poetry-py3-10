FROM python:3.10

LABEL version="{{cookiecutter.version}}"
LABEL author="{{cookiecutter.author}}"
LABEL email="{{cookiecutter.email}}"
LABEL description="{{cookiecutter.project_description}}"

ENV PATH=/{{cookiecutter.project_slug}}/bin:/root/.poetry/bin:${PATH}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

COPY . /{{cookiecutter.project_slug}}
WORKDIR /{{cookiecutter.project_slug}}

# no need for virtualenv in docker
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

CMD ["bash"]
