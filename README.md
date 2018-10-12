# Set Up

This is a simple Python API boilderplate
using [Flask](http://flask.pocoo.org/) and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).
It uses [Pyenv](https://github.com/pyenv/pyenv) and [Pipenv](https://pipenv.readthedocs.io/en/latest/)
for runtime and package management.
It also uses [pytest](https://docs.pytest.org/en/latest/) and [pytest-flask](https://pytest-flask.readthedocs.io/en/latest/)
for unit testing.

You can find detailed documentation on this boilerplate's set-up [here](https://nikgrozev.com/2018/10/12/python-api-with-flask-and-flask-restplus/). 

# Set Up

Install [Pyenv](https://github.com/pyenv/pyenv) following the [official installation instructions](https://github.com/pyenv/pyenv#installation).

Download the proper python version:

```bash
# Installs the version from ".python-version" if not installed 
# Can take some time.
pyenv install
```

Install pipenv:

```bash
pip install --user pipenv
```

Install all dependencies

```bash
pipenv install
```

# Run locally

```bash
# If you haven't already, then start a pipenv shell
pipenv shell

PYTHON_ENV=development python src/main.py
```

Visit Swagger UI on [http://localhost:5000/api/swagger](http://localhost:5000/api/swagger).

# Run unit tests


```bash
# If you haven't already, then start a pipenv shell
pipenv shell

python -m pytest
```