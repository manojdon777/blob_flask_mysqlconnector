import mysql.connector

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def readBLOB(emp_id, photo, bioData):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='localhost', user='admin', password='admin', database='timeDB')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from employee where id = %s"""

        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            image = row[2]
            file = row[3]
            print("Storing employee image and bio-data on disk \n")
            write_file(image, photo)
            write_file(file, bioData)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

photo = 'images/Pink_backed_Pelican1.jpg' #output image file name
biodata = 'images/bio11.txt' #output resume file name
readBLOB(1, photo, biodata)
photo = 'images/Red_Fody2.jpg' #output image file name
biodata = 'images/bio22.txt' #output resume file name
readBLOB(2, photo, biodata)