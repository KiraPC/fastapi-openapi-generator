import sys, json, click, mock
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
@click.option(
    "--file-name",
    "file_name",
    default="openapi.json",
    show_default=True,
    help="The name the openapi file will assume."
)
@click.option(
    "--mock-class",
    "classes_to_mock",
    multiple=True,
    help="Use it to mock a package that is not usefully for the openapi generation and block the fastapi start"
)
def main(app, app_dir, output_dir, file_name, classes_to_mock):
    sys.path.insert(0, app_dir)

    if classes_to_mock:
        for class_to_mock in classes_to_mock:
            mock.patch(class_to_mock).start()

    fastapi: FastAPI = import_from_string(app)

    if not isinstance(fastapi, FastAPI):
        raise NotFastAPIException('The given object is not a FastAPI application')

    with open('{}/{}'.format(output_dir, file_name), 'w+') as openapi:
        openapi.write(json.dumps(fastapi.openapi(), indent=2))
        openapi.close()

if __name__ == "__main__":
    main()
