from flask import Flask, jsonify
from flask_cors import CORS
from clickhouse_driver import Client
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

client = Client(host='clickhouse', port=9000)

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    logger.info("Healthcheck endpoint was called")
    return jsonify({'status': 'OK'}), 200

@app.route("/likes", methods=["GET"])
def get_likes():
    try:
        likes = client.execute('SELECT * FROM likes')
        logger.info("Fetched likes from ClickHouse")
        return jsonify(likes), 200
    except Exception as e:
        logger.error(f"Error fetching likes: {e}")
        return jsonify({'error': 'Failed to fetch likes'}), 500

@app.route("/views", methods=["GET"])
def get_views():
    try:
        views = client.execute('SELECT * FROM views')
        logger.info("Fetched views from ClickHouse")
        return jsonify(views), 200
    except Exception as e:
        logger.error(f"Error fetching views: {e}")
        return jsonify({'error': 'Failed to fetch views'}), 500

if __name__ == "__main__":
    logger.info("Starting the application")
    app.run(host='0.0.0.0', port=50052)