# Database Connection Code
import mysql.connector

def connect_db():
    import mysql.connector

    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="civic_issue_db",
        auth_plugin="mysql_native_password",
        use_pure=True
    )

    return connection

# API 1: Extract department information
def get_departments():
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM departments"
    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

# API 2: Save issue in database
def save_issue(user_id, department_id, issue_type, image_url, location):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO complaints (user_id, department_id, issue_type, image_url, location)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(user_id,department_id,issue_type,image_url,location))
    connection.commit()

    cursor.close()
    connection.close()

    # API 3: Admin can add department
def add_department(name,email):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO departments (name,email)
    VALUES (%s,%s)
    """

    cursor.execute(query,(name,email))
    connection.commit()

    cursor.close()
    connection.close()

    # API 4: Admin filter issues by department
def filter_issues(department_id):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT * FROM complaints
    WHERE department_id=%s
    """

    cursor.execute(query,(department_id,))
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

# API 5: Store user login information
def save_user(name,email,password):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO users (name,email,password)
    VALUES (%s,%s,%s)
    """

    cursor.execute(query,(name,email,password))
    connection.commit()

    cursor.close()
    connection.close()

    # API 6: Update complaint status
def update_status(complaint_id, status):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    UPDATE complaints
    SET status=%s
    WHERE complaint_id=%s
    """

    cursor.execute(query,(status,complaint_id))
    connection.commit()

    cursor.close()
    connection.close()

#Create Complaint
def create_complaint(user_id, department_id, issue_type, image_url, location):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO complaints (user_id, department_id, issue_type, image_url, location)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(user_id,department_id,issue_type,image_url,location))
    connection.commit()

    cursor.close()
    connection.close()

#Get Complaints for Department
def get_department_complaints(department_id):
    print("Connecting to database...")

    connection = connect_db()

    print("Connection established")

    cursor = connection.cursor(dictionary=True)

    print("Cursor created")

    query = """
    SELECT * FROM complaints
    WHERE department_id=%s
    """

    cursor.execute(query,(department_id,))
    print("Query executed")

    result = cursor.fetchall()
    print("Data fetched")

    cursor.close()
    connection.close()

    return result
#Update Complaint Status
def update_status(complaint_id,status):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    UPDATE complaints
    SET status=%s
    WHERE complaint_id=%s
    """

    cursor.execute(query,(status,complaint_id))
    connection.commit()

    cursor.close()
    connection.close()

#Get Department Email
def get_department_email(complaint_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    SELECT d.email
    FROM complaints c
    JOIN departments d
    ON c.department_id = d.department_id
    WHERE c.complaint_id=%s
    """

    cursor.execute(query,(complaint_id,))
    email = cursor.fetchone()

    cursor.close()
    connection.close()

    return email