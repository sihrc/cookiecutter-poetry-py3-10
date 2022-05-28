#! /usr/bin/env python
import io
import json
import logging
import os
import sys
import typing as t
from contextlib import redirect_stdout
from multiprocessing import Process
from pathlib import Path

from poetry.console import Application

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def run_poetry_command(*args_list: t.Iterable[str]):
    app = Application()
    app.config.set_terminate_after_run(False)
    output_buffer = io.StringIO()

    with redirect_stdout(output_buffer):
        sys.argv[1:] = args_list
        logging.info(f"Poetry command: {' '. join(args_list)}")
        app.run()

    stdout = output_buffer.getvalue()

    # remove exit code
    return stdout.split()


def try_remove(path: t.Union[str, Path]):
    # Coerce into path obj
    path: Path = Path(path)

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
    path: Path = Path(path)
    if not path.is_file():
        raise ValueError(f"Invalid path to json file {path}")

    with path.open("r") as f:
        settings_json: t.Dict = json.load(f)

    settings_json.update(values)

    with path.open("w") as f:
        json.dump(settings_json, f, indent=2)

    return settings_json


def main():
    os.system("git init")
    os.system("git checkout -b main")

    # Commands to run
    for command in (
        # ("config", "virtualenvs.in-project", "true", "--local"),
        ("add", "--dev", "pytest", "black", "isort", "ipdb"),
        ("update",),
        ("install",),
    ):
        run_poetry_command(*command)

    # TODO: Handle vscode / dotenv options
    if "{{ cookiecutter.use_vscode }}" == "y":
        logging.info("Setting up vscode python interpreter path")
        run_poetry_command("add", "python-dotenv")

        # Fetch path to python interpreter for this poetry env
        path = run_poetry_command("env", "info", "--path")[0]

        logging.info(f"Setting python interpreter path to {path}")

        # Add environment python interpreter to vscode settings.json
        updated_settings = update_json(
            Path(".vscode", "settings.json"), {"python.defaultInterpreterPath": path}
        )
        logging.info(f"vscode settings successfully updated {updated_settings}")
    else:
        logging.info("No vscode: deleting .vscode settings directory")
        # Remove .vscode/
        try_remove(".vscode")

    if "{{ cookiecutter.use_dotenv }}" != "y":
        # Remove .env & config.py
        logging.info("No dotenv: deleting boilerplate .env and config.py")
        try_remove(Path("{{ cookiecutter.project_slug }}", "config.py"))

    with open(".gitignore", "a") as f:
        f.write(".vscode/\n")

    p = Process(target=run_poetry_command, args=("run", "pre-commit", "install", "-f"))
    p.start()
    p.join()

    os.system("git add -A; git commit -m 'Cut a cookie from a cookiecutter'")


if __name__ == "__main__":
    main()
