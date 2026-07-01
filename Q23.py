#PRACTICAL
#Q-23
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor",
  database="WORKER"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE IF NOT EXISTS EMPLOYEE (E_ID VARCHAR(10), E_NAME VARCHAR(70), E_SAL INT, E_DEPT VARCHAR(30), E_LOC VARCHAR(70))")

except mysql.connector.Error as err:
    print("There is an error in MySQL execution: {}".format(err))
    exit()

sql = "INSERT INTO EMPLOYEE (E_ID, E_NAME, E_SAL, E_DEPT, E_LOC) VALUES (%s, %s, %s, %s, %s)"

while True:
    E_ID = input("Please enter Employee ID (up to 20 CHARACTER, enter STOP to exit the DATA entry): ")
    if E_ID.upper() == 'STOP':
        break;
    E_NAME = input("Please enter Name (up to 70 CHARACTER): ")
    E_SAL = int(input("Please enter Salary (INT): "))
    E_DEPT = input("Please enter Depertment (30 CHARACTER MAX): ")
    E_LOC = input("Please enter Location (up to 50 CHARACTER): ")    
    val = (E_ID, E_NAME, E_SAL, E_DEPT, E_LOC)
    
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    except mysql.connector.Error as err:
        print("There is an error in MySQL insert: {}".format(err))
        exit()

print("Displaying Employee Data For Office Location 'PUNE' or 'NOIDA' or 'DELHI' Salary more than 57000 ===>>>>")
mycursor.execute("SELECT *, E_SAL * 0.33 AS BONUS FROM EMPLOYEE WHERE E_LOC IN ('PUNE', 'NOIDA', 'DELHI') AND E_SAL > 57000")
allrows = mycursor.fetchall()
for row in allrows:
    print("Employee ID: ", row[0])
    print("Employee Name: ", row[1])
    print("Employee Salary: ", row[2])
    print("Employee Bonus: ", row[5])
    print("Employee Department: ", row[3])
    print("Employee Location: ", row[4])
    print("==============================")
