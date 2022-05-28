import mysql.connector

conn = mysql.connector.connect(username='root', password='chocobar@6',host='localhost',database='facedb')
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()

