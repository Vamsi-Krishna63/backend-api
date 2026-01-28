from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/greet")
def greet():
    return jsonify({"message": "Hello from backend"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)