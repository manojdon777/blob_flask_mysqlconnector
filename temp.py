from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'imageDB',
    'autocommit': True,
}

# Function to create a connection to the MySQL database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connected to MySQL database")
    except Error as e:
        print(f"Error: {e}")
    return connection

# Function to execute a query
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        print("Query executed successfully")
    except Error as e:
        print(f"Error: {e}")

# Create the 'imageDB' database and 'image' table
def create_database_table():
    connection = create_connection()
    
    # Create database 'imageDB'
    create_db_query = "CREATE DATABASE IF NOT EXISTS imageDB"
    execute_query(connection, create_db_query)

    # Switch to 'imageDB'
    db_config['database'] = 'imageDB'
    connection = create_connection()

    # Create table 'image'
    create_table_query = """
    CREATE TABLE IF NOT EXISTS image (
        id INT AUTO_INCREMENT PRIMARY KEY,
        file_path VARCHAR(255) NOT NULL
    )
    """
    execute_query(connection, create_table_query)

    # Close the connection
    connection.close()

create_database_table()

@app.route('/')
def index():
    return render_template('index.html')

# The rest of your application code for image upload goes here
