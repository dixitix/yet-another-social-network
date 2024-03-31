FROM python:3.9

WORKDIR /auth-server

COPY . /auth-server

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
