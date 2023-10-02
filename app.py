from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/hybrid-credit', methods=['POST'])
def api():
    if request.data:
        data = dict(request.get_json())
        if (len(data.keys()) == 2) and ('user' in data) and ('prompt' in data):
            if isinstance(data['user'], str) and isinstance(data['prompt'], str):
                return jsonify(data), 200
            else:
                return "Please provide string parameters", 400
        else:
            return "Please provide a valid body parameters"
    else:
        return "Please provide a body parameters", 400


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
