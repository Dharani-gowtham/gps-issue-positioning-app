from flask import Flask, request, jsonify
from database import push_issue, get_issue_list, detailed_issue_list

app = Flask(__name__)


@app.route('/add-issue', methods=['POST'])
def add_issue():
    data = request.get_json()
    response = push_issue(data)
    return response, 200


@app.route('/view-issue', methods=['GET'])
def view_issue():
    data = get_issue_list()
    return data, 200

@app.route('/details', methods=['GET'])
def details():
    data = detailed_issue_list()
    return data, 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

