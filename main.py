from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello {name}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
