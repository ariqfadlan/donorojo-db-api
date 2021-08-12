# Donorojo Database API

A simple read-only REST API written in Python.
WebServer is provided by FastAPI.
Database migration is provided by Alembic.

Tested on Python 3.9 on GNU/Linux.

## Get started
Create the usual virtual environment and install requirements accordingly.
For running web server, execute:
```bash
$ uvicorn main:app
```

For development, add `--reload` parameter to let it watch changes inside workspace.
```bash
$ uvicorn main:app --reload
```

