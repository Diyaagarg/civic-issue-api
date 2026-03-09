from flask import Flask, request, jsonify
from database import *

app = Flask(__name__)


# API 1 - Get departments
@app.route("/departments", methods=["GET"])
def departments():
    data = get_departments()
    return jsonify(data)


# API 2 - Save issue
@app.route("/save_issue", methods=["POST"])
def save_issue_api():
    data = request.json

    save_issue(
        data["user_id"],
        data["department_id"],
        data["issue_type"],
        data["image_url"],
        data["location"]
    )

    return jsonify({"message":"Issue saved"})


# API 3 - Add department
@app.route("/add_department", methods=["POST"])
def add_department_api():
    data = request.json

    add_department(data["name"], data["email"])

    return jsonify({"message":"Department added"})


# API 4 - Filter issues
@app.route("/issues/<int:department_id>", methods=["GET"])
def filter_issues_api(department_id):
    data = filter_issues(department_id)
    return jsonify(data)


# API 5 - Save user
@app.route("/save_user", methods=["POST"])
def save_user_api():
    data = request.json

    save_user(data["name"], data["email"], data["password"])

    return jsonify({"message":"User saved"})


if __name__ == "__main__":
    app.run(debug=True)