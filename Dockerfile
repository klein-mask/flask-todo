FROM python:3.8.3-slim-buster

WORKDIR /work

COPY requirements.txt /work/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000


CMD [ "python", "/app/main.py" ]