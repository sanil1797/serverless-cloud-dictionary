from flask import Flask, jsonify
import time
import logging
import sys
import os

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("/var/log/monitoring-demo-app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

@app.route("/")
def home():
    logging.info("Home endpoint hit")
    return jsonify({"service": "monitoring-demo-app", "status": "running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/error")
def error():
    logging.error("Simulated error endpoint triggered")
    return jsonify({"error": "simulated failure"}), 500

@app.route("/slow")
def slow():
    logging.warning("Simulating slow response (10s)")
    time.sleep(10)
    return jsonify({"status": "slow response completed"})

@app.route("/crash")
def crash():
    logging.critical("Crash endpoint triggered - exiting process")
    os._exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
