import mysql.connector

print("Starting connection test...")

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="civic_issue_db",
    auth_plugin="mysql_native_password",
    use_pure=True
)

print("Connected successfully!")

conn.close()