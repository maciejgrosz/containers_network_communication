from flask import Flask
from datetime import datetime
import requests
import time


app = Flask(__name__)
log_url = "http://172.18.0.3:5000/list"


@app.route("/", methods=["GET"])
def home():
    now = datetime.now()
    message = f'Today is: {now.strftime("%m/%d/%Y, %H:%M:%S")}'
    r = requests.post(log_url, data=message)
    return f"{message}"


if __name__ == "__main__":
    app.run()
