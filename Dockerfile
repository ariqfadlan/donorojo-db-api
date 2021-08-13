FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

#RUN apt-get update && \
    #apt-get install libpq-dev -y && \
    #rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY app /app/app
COPY ./main.py /app
