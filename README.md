# cookiecutter-poetry-py3-10

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template used to generate Python 3.10+ poetry projects.


## Features
#### Poetry
local directory installation for vscode interpreter magic.

#### Docker
Dockerfile with python 3.10 base image and package installation

#### Pre-commit
Python's Isort for import formatting
Python's Black for strict formatting

#### vscode settings (optional)
VSCode settings that use black and the local poetry python package for auto-completes and module discovery

#### dotenv loading (optional)
For application type packages that have .env provided runtime configurations


## Installation
```bash
pip3 install cookiecutter
```

## Usage
```bash
cookiecutter gh:sihrc/cookiecutter-poetry-py3-10
```

The cookiecutter generation hooks will automatically setup all features and dependency necessary for this project.

## Pre-commit Hooks
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        name: isort (python)
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
```
