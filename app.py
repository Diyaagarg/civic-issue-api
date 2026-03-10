from flask import Flask, request, jsonify
from database import (
    get_departments,
    save_issue,
    add_department,
    filter_issues,
    save_user,
    update_status
)

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Civic Issue API is running"})


@app.route("/departments", methods=["GET"])
def departments():
    data = get_departments()
    return jsonify(data)


@app.route("/save_issue", methods=["POST"])
def save_issue_api():
    data = request.get_json()

    save_issue(
        data["user_id"],
        data["department_id"],
        data["issue_type"],
        data.get("image_url"),
        data["location"]
    )

    return jsonify({"message": "Issue saved"}), 201


@app.route("/add_department", methods=["POST"])
def add_department_api():
    data = request.get_json()

    add_department(
        data["department_name"],
        data["email"]
    )

    return jsonify({"message": "Department added"}), 201


@app.route("/issues/<int:department_id>", methods=["GET"])
def filter_issues_api(department_id):
    data = filter_issues(department_id)
    return jsonify(data)


@app.route("/save_user", methods=["POST"])
def save_user_api():
    data = request.get_json()

    save_user(
        data["name"],
        data["email"],
        data["password"],
        data.get("department_id")
    )

    return jsonify({"message": "User saved"}), 201


@app.route("/update_status", methods=["PUT"])
def update_status_api():
    data = request.get_json()

    update_status(
        data["complaint_id"],
        data["status"]
    )

    return jsonify({"message": "Status updated"})


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))