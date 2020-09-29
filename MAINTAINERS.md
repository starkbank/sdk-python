## Deploy

### Create a source distribution:

Run inside the project directory:
```sh
python setup.py sdist
```

### Install twine:

```sh
pip install twine
```

### Upload package to pypi:

```sh
twine upload dist/*
```
