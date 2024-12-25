import mysql.connector

# Connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        passwd="admin123",
        db="iesa_db"
    )

# Fetch user data
def validate_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM user_data WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()[0]
    conn.close()
    return result > 0
