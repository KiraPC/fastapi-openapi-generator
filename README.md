### What this repository contains

A Command Line Interface to save openapi file from a FastAPI application

### Installation: 

install the package
```
pip install fastapi-openapi-generator
```

### How to use
```
fastapi-openapi-gen main:app \
    --app-dir= # The path to mounth in the python path to import the module. \
    --output-dir= # The path where store the openapi template. \
    --file-name= # The name the openapi file will assume.
    --mock-class= # Use it to mock a package that is not usefully for the openapi generation and block the fastapi start
```
