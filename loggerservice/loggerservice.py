from flask import Flask
from datetime import datetime
import requests
from flask import request

app = Flask(__name__)
logs = []


@app.route("/usage.log", methods=["GET", "POST"])
def home():
    now = datetime.now()
    r = requests.get("http://172.18.0.2:5000")
    logs.append(r.text)

    #    y = requests.args.get()
    return "\n".join(logs)


if __name__ == "__main__":
    app.run()
