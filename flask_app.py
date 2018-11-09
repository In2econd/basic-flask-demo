import json
from   flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Test GET and POST requests """

    if request.method == 'GET':
        return jsonify({'success': True})

    elif request.method == 'POST':
        try:
            # Expects data to be structured as follows
            # {'request': 'Example String'}
            data = json.loads(request.data)
            response = [{'success': True}, {'request': data['request']}]
            return jsonify(response)
        except Exception:
            return jsonify({'success': False})


if __name__ == '__main__':
    """ Start Flask app on default port 5000 """

    app.run('0.0.0.0')