# PUNTUACIONES

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2oKqn",
  database="gp"
)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO `gp`.`student` (`name`, `major`) VALUES ('Tes34432', 't34234234est')")
mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mydb.commit()