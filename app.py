import json

from flask import Flask, request, make_response
from call_contact import get_caller_name
from colored_exception import logException

app = Flask(__name__)


@app.route('/callerName', methods=['POST'])
def get_caller_name_endpoint():
    try:
        text = request.get_json()['text']
        print("text is" + text)

        name = get_caller_name(text)
        print("name is " + name)
        return json.dumps({"data": name})

    except Exception as e:
        logException(str(e))
        return json.dumps({"exception": str(e)})


@app.route('/', methods=['GET'])
def hello_world_endpoint():
    return json.dumps({"message": "hello world"})


if __name__ == '__main__':
    print("YES")
    app.run(host='0.0.0.0', port=5000)
