# pylint: disable=line-too-long
"""
    :author: Pasquale Carmone Carbone

    Setup module
"""
import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open('requirements.txt', 'r') as fin:
    REQS = fin.read().splitlines()

setuptools.setup(
    setup_requires=['setuptools-git-version'],
    version_format='{tag}',
    name="fastapi-openapi-generator",
    author="Pasquale Carmine Carbone",
    author_email="pasqualecarmine.carbone@gmail.com",
    description="A Command Line Interface to save openapi file from a FastAPI application",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/KiraPC/fastapi-openapi-generator",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=['venv', 'fastapi-openapi-generator.egg-info', 'build']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'fastapi-openapi-gen = generator.main:main'
        ]
    },
    python_requires='>=3.0',
    install_requires=REQS
)
