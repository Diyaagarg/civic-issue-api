# Civic Issue Reporting API

A Flask-based REST API for reporting and managing civic issues such as potholes, garbage, and water leakage.  
The system stores complaints in a database and allows departments to retrieve and manage them.

## Technologies Used
- Python
- Flask
- MySQL
- REST API
- JSON

## Project Structure
civic-issue-api
│
├── app.py                # Main Flask API
├── database.py           # Database connection & queries
├── test_connection.py    # Database connection test
├── test_db.py            # Database testing
└── README.md             # Project documentation

## API Endpoints

### Get Departments
GET /departments

Returns a list of civic departments.

### Save Issue
POST /save_issue

Submit a new civic complaint.

Example JSON:

{
  "citizen_name": "Rahul",
  "issue_type": "Pothole",
  "location": "Sector 15",
  "description": "Large pothole causing traffic"
}

## How to Run the Project

1. Install dependencies

pip install flask mysql-connector-python

2. Run the Flask server

python app.py

3. Open in browser

http://127.0.0.1:5000/departments

## Author
Diya Garg