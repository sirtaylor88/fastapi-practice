# FastAPI Practice

## Project structure with poetry

```bash
fastapi-practice
│   README.md
│   pyproject.toml
│   pyproject.toml
│   poetry.lock
|
└───fastapi_practice
│   │   __init__.py
│   │   main.py
```

## Install FastAPI

Install poetry to manage dependencies

```bash
pip install poetry
```

Init `pyproject.toml` using `poetry`

```bash
poetry init
```

Install `FastAPI` framework and `uvicorn`

```bash
poetry add fastapi "uvicorn[standard]"
```

## Run server

```bash
uvicorn fastapi_practice.main:app --reload
```
