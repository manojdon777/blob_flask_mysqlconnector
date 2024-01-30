from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin",
        database="timeDB"
    )
except mysql.connector.Error as error:
    print("Failed to connect to database - {}".format(error))

cursor = mydb.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS imageDB')

cursor.execute('USE imageDB')

cursor.execute('''
            CREATE TABLE IF NOT EXISTS image (
                id INT AUTO_INCREMENT PRIMARY KEY,
                imgFile LONGBLOB
            )
            ''')

mydb.commit()

# sql_insert_blob_query = """INSERT INTO employee (id, image) VALUES (%s,%s)"""


app = Flask(__name__)

@app.route("/")
def index():
    # return "<p>Hello, World!</p>"
    return render_template('index.html')

def convertToBinaryData(filename):
	# Convert digital data to binary format
	with open(filename, 'rb') as file:
		binaryData = file.read()
	return binaryData
    
@app.route("/save")
def save():

    # cursor = mydb.cursor()
    sql_insert_blob_query = """INSERT INTO image (imgFile) VALUES (%s)"""

    img_file = request.files['imgFile']
    image = convertToBinaryData(img_file)

    # Convert data into tuple format
    insert_blob_tuple = (Picimageture, file)
    result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
    mydb.commit()
    print("Image and file inserted successfully as a BLOB into python_employee table", result)


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0')
