from flask import Flask, request
from datetime import datetime
import requests

app = Flask(__name__)
url="http://172.18.0.3:5000"
log_url="http://172.18.0.3:5000"
test = {'somekey': 'somevalue'}

@app.route("/", methods=['GET', 'POST'])
def home():
    now = datetime.now()
    message = f'Today is: {now.strftime("%m/%d/%Y, %H:%M:%S")}'
    test = {'somekey': 'somevalue'}
    # r = requests.get(log_url)
    r = requests.post(log_url,  data = message )
    return f'{message}'

if __name__ == "__main__":
    app.run()
