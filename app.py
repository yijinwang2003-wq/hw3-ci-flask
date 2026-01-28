from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "broken"}), 200


@app.get("/hello")
def hello():
    return jsonify({"message": "hello world"}), 200


@app.get("/add")
def add():
    return jsonify({"result": 1 + 2}), 200


if __name__ == "__main__":
    app.run(debug=True)
