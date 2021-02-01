rm -rf .eggs/
rm -rf fastapi_openapi_generator.egg-info/
rm -rf dist/

git pull

python setup.py sdist
twine upload dist/*