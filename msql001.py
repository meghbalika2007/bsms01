import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Meghbalika@2007",
  database="school"
)
mycursor = mydb.cursor()

mycursor.execute("select * from student;")

for x in mycursor:
  print("Student id: ",x[0])
  print("Student name: ",x[1])
  print("Student dob: ",x[2])
  print("Student stream: ",x[3])
