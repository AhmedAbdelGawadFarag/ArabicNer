import json

from flask import Flask, request, make_response
from call_contact import get_caller_name

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello():
    print("request data")
    text = request.get_json()['data']
    name = get_caller_name(text)
    return json.dumps({"data": name})
