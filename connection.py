import os
from dotenv import load_dotenv
load_dotenv()

def dbconnection():
    server = 'DNTSDB01'
    database = 'dauntlessIT'
    connection_username = os.environ.get("CONNECTION_USERNAME")
    connection_password = os.environ.get("SECRET_KEY")
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={connection_username};PWD={connection_password}'
    return connection_string