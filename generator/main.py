import sys
import json
import click
from fastapi import FastAPI
from uvicorn.importer import import_from_string
from generator.lib.exceptions import NotFastAPIException

@click.command()
@click.argument("app")
@click.option(
    "--app-dir",
    "app_dir",
    default=".",
    show_default=True,
    help="Look for APP in the specified directory, by adding this to the PYTHONPATH."
    " Defaults to the current working directory."
)
@click.option(
    "--output-dir",
    "output_dir",
    default=".",
    show_default=True,
    help="The folder where the swagger is stored."
)
def main(app, app_dir, output_dir):
    sys.path.insert(0, app_dir)

    fastapi: FastAPI = import_from_string(app)

    if not isinstance(fastapi, FastAPI):
        raise NotFastAPIException('The given object is not a FastAPI application')

    with open('{}/openapi.json'.format(output_dir), 'w+') as openapi:
        openapi.write(json.dumps(fastapi.openapi(), indent=2))

if __name__ == "__main__":
    main()
