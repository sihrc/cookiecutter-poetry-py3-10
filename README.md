# cookiecutter-poetry-py3-10

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template used to generate Python 3.10+ poetry projects.

## Features

#### Poetry

local directory installation for vscode interpreter magic.

#### Docker

Dockerfile with python 3.10 base image and package installation

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
cookiecutter gh:IndicoDataSolutions/cookiecutter-poetry-py3-10
```

The cookiecutter generation hooks will automatically setup all features and dependency necessary for this project.

## Pre-commit Hooks
```
$ pip install pre-commit
$ pre-commit install
```