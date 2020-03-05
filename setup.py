from os import path
from setuptools import setup, find_packages


with open(path.join(path.dirname(__file__), "README.md")) as readme:
    README = readme.read()


setup(
    name="starkbank",
    packages=find_packages(),
    include_package_data=True,
    description="SDK to facilitate python integrations with Stark Bank",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/starkbank/sdk-python.git",
    author="Stark Bank",
    author_email="developers@starkbank.com",
    keywords=["stark bank", "starkbank", "sdk", "open banking", "openbanking"],
    version="2.0.0"
)


### Create a source distribution:

#Run ```python setup.py sdist``` inside the project directory.

### Install twine:

#```pip install twine```

### Upload package to pypi:

#```twine upload dist/*```

