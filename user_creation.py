import pyodbc
import bcrypt
from connection import dbconnection

def create_user(username, password):
    connection_string = dbconnection()
    with pyodbc.connect(connection_string) as connection:
        with connection.cursor() as cursor:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            try:
                cursor.execute("INSERT INTO Test_Users (Username, Password) VALUES (?, ?)", (username, hashed))
                connection.commit()
                return True
            except pyodbc.IntegrityError:
                # Handle duplicate usernames
                return False
            except pyodbc.Error as e:
                # Handle other database errors
                print("Database error:", e)
                return False
