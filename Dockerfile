FROM python:3.8.3-slim-buster

RUN pip install --upgrade pip && \
    pip install flask flask_sqlalchemy

EXPOSE 5000

WORKDIR /app

CMD [ "python", "/app/main.py" ]