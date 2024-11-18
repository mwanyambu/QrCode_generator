import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="R00tPassword",
)
cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS qrdatabase")