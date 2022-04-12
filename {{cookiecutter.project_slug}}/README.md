# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

Built on: Poetry, Docker, Python3

Authors: <br>
{{ cookiecutter.author }} <{{ cookiecutter.email }}>

## Getting started

```bash
$ poetry install

# Test Installation
$ poetry run python3 -c "import {{ cookiecutter.project_slug}}; print({{cookiecutter.project_slug}})"
```

## pre-commit hooks

Configured pre-commit hooks

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        name: isort (python)
```

Usage:

```bash
$ pre-commit install
# Example usage outside of git hooks
$ pre-commit run -a
```
