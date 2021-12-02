import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Behnam",
  password="my@dmin.2002",
  database="library"
)

mycursor = mydb.cursor()

sql = "INSERT INTO members (FirstName,LastName,NationalCode,PhoneNumber) VALUES (%s,%s,%s, %s)"
val = ("Reza", "Hassani" , "0152314595" , "9125463557")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")