from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👈 THIS LINE FIXES EVERYTHING

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/greet")
def greet():
    return jsonify({"message": "Hello from backend"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
