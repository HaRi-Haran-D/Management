import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    port=3306,
    auth_plugin="mysql_native_password",
    use_pure=True,
    ssl_disabled=True,
    connection_timeout=5,
)

cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS manage")

cursor.close()
database.close()

print("finished")
