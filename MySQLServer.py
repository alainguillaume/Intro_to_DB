import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'smart123'
)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Data base created successully")

except mysql.connection.error:
    print(f"Failed to connect to MySQL")

except mysql.connector.Error as e:
    print(f"Failed to connect to MySQL: {e}")
mycursor.close()
mydb.close()