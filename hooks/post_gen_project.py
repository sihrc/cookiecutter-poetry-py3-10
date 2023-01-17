#! /usr/bin/env python
import json
import logging
import sys
import typing as t
from pathlib import Path

import sh

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def run_poetry_command(*args_list: t.Iterable[str]):
    return str(sh.poetry(*args_list))


def try_remove(path: t.Union[str, Path]):
    # Coerce into path obj
    path = Path(path)

    # Delete either file or dir (true if exists)
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        for filepath in path.iterdir():
            filepath.unlink()
        path.rmdir()


def update_json(
    path: t.Union[str, Path], values: t.Dict[str, t.Union[t.Dict, t.Any]]
) -> t.Dict:
    """Update a json file with dictionary of values given json path

    Args:
        path (t.Union[str, Path]): path to json file
        values: Kwargs representing values to insert

    Raises:
        ValueError: Invalid path

    Returns:
        settings_json (t.Dict): updated settings dictionary
    """
    path = Path(path)
    if not path.is_file():
        raise ValueError(f"Invalid path to json file {path}")

    with path.open("r") as f:
        settings_json: t.Dict = json.load(f)

    settings_json.update(values)

    with path.open("w") as f:
        json.dump(settings_json, f, indent=2)

    return settings_json


def main():
    sh.git("init")
    sh.git.checkout("-b", "main")

    # Commands to run
    for command in (
        (
            "config",
            "virtualenvs.in-project",
            "true",
        ),
        ("add", "--dev", "pytest", "black", "isort", "ipdb"),
        ("update",),
        ("install",),
    ):
        run_poetry_command(*command)

    getattr(sh, "pre-commit").install("-f")
    sh.git.add("-A")
    sh.git.commit("-m", "'Cut a cookie from a cookiecutter'")


if __name__ == "__main__":
    main()
