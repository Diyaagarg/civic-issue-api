import os
import mysql.connector


def connect_db():
    connection = mysql.connector.connect(
        host=os.getenv("MYSQLHOST"),
        port=int(os.getenv("MYSQLPORT")),
        user=os.getenv("MYSQLUSER"),
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        connection_timeout=30,
        auth_plugin='mysql_native_password'
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


def get_department_by_id(department_id):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT * FROM departments
    WHERE department_id = %s
    """

    cursor.execute(query, (department_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


def get_department_by_issue_type(issue_type):
    issue_type = issue_type.lower().strip()

    if "pothole" in issue_type or "road" in issue_type:
        department_id = 1
    elif "water" in issue_type or "pipe" in issue_type:
        department_id = 2
    elif "electricity" in issue_type or "street light" in issue_type or "power" in issue_type:
        department_id = 3
    elif "garbage" in issue_type or "sanitation" in issue_type or "waste" in issue_type:
        department_id = 4
    else:
        return None

    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT * FROM departments
    WHERE department_id = %s
    """

    cursor.execute(query, (department_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

# API 2: Save issue in database
def save_issue(email, department_id, issue_type, image_url, location):
    try:
        connection = connect_db()
        cursor = connection.cursor()

        # 1: Get user_id from email
        user_query = "SELECT user_id FROM users WHERE email = %s"
        cursor.execute(user_query, (email,))
        user = cursor.fetchone()

        if not user:
            cursor.close()
            connection.close()
            return {"error": "User not found"}

        user_id = user[0]

        # 2: save complaint using user_id
        query = """
        INSERT INTO complaints (user_id, department_id, issue_type, image_url, location)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (user_id, department_id, issue_type, image_url, location))
        connection.commit()

        cursor.close()
        connection.close()

        return {"message": "Issue saved"}

    except mysql.connector.Error as err:
        return {"error": str(err)}

    except Exception as e:
        return {"error": str(e)}

# 
def get_user_history(email):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT c.complaint_id, c.issue_type, c.image_url, c.location, c.status, c.department_id
    FROM complaints c
    JOIN users u ON c.user_id = u.user_id
    WHERE u.email = %s
    ORDER BY c.complaint_id DESC
    """

    cursor.execute(query, (email,))
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

# API 3: Admin can add department
def add_department(department_name, email):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO departments (department_name, email)
    VALUES (%s, %s)
    """

    cursor.execute(query, (department_name, email))
    connection.commit()

    cursor.close()
    connection.close()


# API 4: Admin filter issues by department
def filter_issues(department_id):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT * FROM complaints
    WHERE department_id = %s
    """

    cursor.execute(query, (department_id,))
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result


# API 5: Store user login information
def save_user(name, email, password, department_id=None):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO users (name, email, password, department_id)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, password, department_id))
    connection.commit()

    cursor.close()
    connection.close()


# API 6: Update complaint status
def update_status(complaint_id, status):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    UPDATE complaints
    SET status = %s
    WHERE complaint_id = %s
    """

    cursor.execute(query, (status, complaint_id))
    connection.commit()

    cursor.close()
    connection.close()


# Extra: Get complaints for department
def get_department_complaints(department_id):
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT * FROM complaints
    WHERE department_id = %s
    """

    cursor.execute(query, (department_id,))
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result


# Extra: Get department email from complaint
def get_department_email(complaint_id):
    connection = connect_db()
    cursor = connection.cursor()

    query = """
    SELECT d.email
    FROM complaints c
    JOIN departments d
    ON c.department_id = d.department_id
    WHERE c.complaint_id = %s
    """

    cursor.execute(query, (complaint_id,))
    email = cursor.fetchone()

    cursor.close()
    connection.close()
    return email[0] if email else None