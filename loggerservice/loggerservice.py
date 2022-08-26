from flask import Flask, jsonify
from datetime import datetime
import requests
from flask import request

app = Flask(__name__)
logs = []


@app.route("/list", methods=["POST"])
def list():
    r = request.data.decode("utf-8")
    logs.append(r)
    return jsonify(success=True)


@app.route("/usage.log")
def home():
    return "<br>".join(logs)


if __name__ == "__main__":
    app.run()
