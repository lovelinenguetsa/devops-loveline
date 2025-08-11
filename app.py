# app.py - Simple Flask web app
# Flask is a small Python web framework.

from flask import Flask
app = Flask(__name__)

@app.route("/")  # This means "when someone goes to the home page"
def home():
    return "Hello from DevOps!"

@app.route("/health")  # Health check endpoint for Kubernetes
def health():
    return "OK", 200

# Only run the app if the file is executed directly (not imported)
if __name__ == "__main__":
    # Host 0.0.0.0 means "listen to all network connections"
    app.run(host="0.0.0.0", port=5000)
