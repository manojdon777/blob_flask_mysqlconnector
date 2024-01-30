import mysql.connector

def convertToBinaryData(filename):
	# Convert digital data to binary format
	with open(filename, 'rb') as file:
		binaryData = file.read()
	return binaryData

def insertBLOB(emp_id, name, photo, biodataFile):
	print("Inserting BLOB into python_employee table")
	try:
		connection = mysql.connector.connect(host='localhost', user='admin', password='admin', database='timeDB')

		cursor = connection.cursor()
		cursor.execute('CREATE DATABASE IF NOT EXISTS imageDB')
		connection.commit()

		sql_insert_blob_query = """INSERT INTO employee (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

		empPicture = convertToBinaryData(photo)
		file = convertToBinaryData(biodataFile)

		# Convert data into tuple format
		insert_blob_tuple = (emp_id, name, empPicture, file)
		result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
		connection.commit()
		print("Image and file inserted successfully as a BLOB into python_employee table", result)

	except mysql.connector.Error as error:
		print("Failed inserting BLOB data into MySQL table {}".format(error))

	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
			print("MySQL connection is closed")

photo = 'images/Pink_backed_Pelican.jpg'
biodata = 'images/bio1.txt'
insertBLOB(1, "Eric", photo, biodata)
photo = 'images/Red_Fody.jpg'
biodata = 'images/bio2.txt'
insertBLOB(2, "Scott", photo, biodata)