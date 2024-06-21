FROM python:3.9-slim

WORKDIR /statistics-server

COPY . /statistics-server

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 50052

CMD ["python", "app.py" ]