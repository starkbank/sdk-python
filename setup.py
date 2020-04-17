from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as readme:
    README = readme.read()

about = {}
with open(path.join(here, "starkbank", "__version__.py")) as versionfile:
    exec(versionfile.read(), about)

setup(
    name="starkbank",
    packages=find_packages(),
    include_package_data=True,
    description="SDK to facilitate Python integrations with Stark Bank",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT License",
    url="https://github.com/starkbank/sdk-python",
    author="Stark Bank",
    author_email="developers@starkbank.com",
    keywords=["stark bank", "starkbank", "sdk", "open banking", "openbanking", "banking", "open", "stark"],
    version=about["__version__"],
    install_requires=[
        "requests==2.22.0",
        "starkbank-ecdsa==1.0.0",
    ],
)


### Create a source distribution:

#Run ```python setup.py sdist``` inside the project directory.

### Install twine:

#```pip install twine```

### Upload package to pypi:

#```twine upload dist/*```

