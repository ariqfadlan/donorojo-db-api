FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim

RUN apt-get update && \
    apt-get install libpq-dev gcc -y && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

RUN apt-get remove gcc -y && \
    apt-get autoremove -y

COPY ./alembic.ini /app
COPY scripts/prestart.sh /app

COPY app /app/app
COPY migrations /app/migrations
COPY ./main.py /app
