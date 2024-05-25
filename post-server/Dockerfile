FROM python:3.9-slim

WORKDIR /post-server

COPY . /post-server

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 50051

CMD ["python", "app.py"]
