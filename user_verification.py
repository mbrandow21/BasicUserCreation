import pyodbc
import bcrypt
from connection import dbconnection

def verify_user(username, password):
    connection_string = dbconnection()
    with pyodbc.connect(connection_string) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT Password FROM Test_Users WHERE username=?", (username,))
            row = cursor.fetchone()

            # If no user found
            if not row:
                return None

            stored_hashed_password = row[0].decode('utf-8')
            # Validate the password
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                return True
            else:
                return False
