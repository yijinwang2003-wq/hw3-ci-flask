from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health(  ):              # 多余的空格
            return jsonify({"status": "ok"}), 200    # 错误的缩进



@app.get("/hello")
def hello():
    return jsonify({"message": "hello world"}), 200


@app.get("/add")
def add():
    return jsonify({"result": 1 + 2}), 200


if __name__ == "__main__":
    app.run(debug=True)
