FROM python:3.9-slim

WORKDIR /auth-server

COPY . /auth-server

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
