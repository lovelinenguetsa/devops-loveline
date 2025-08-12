# app.py - Simple Flask web app
# Flask is a small Python web framework.

from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Create a counter metric: counts number of requests to home page
home_requests = Counter('home_requests_total', 'Total requests to home endpoint')

@app.route("/")  # This means "when someone goes to the home page"
def home():
    home_requests.inc()  # Increment counter
    return "Hello from DevOps with metrics!"

@app.route("/health")  # Health check endpoint for Kubernetes
def health():
    return "OK", 200

@app.route("/metrics")
def metrics():
    # Prometheus will scrape this endpoint
    return generate_latest(), 200
# Only run the app if the file is executed directly (not imported)
if __name__ == "__main__":
    # Host 0.0.0.0 means "listen to all network connections"
    app.run(host="0.0.0.0", port=5000)
