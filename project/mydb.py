print("STEP 1: file started")

import mysql.connector
print("STEP 2: mysql.connector imported")

print("STEP 3: trying to connect...")

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    port=3306,
    auth_plugin="mysql_native_password",
    use_pure=True,
    ssl_disabled=True,
    connection_timeout=5
)

print("STEP 4: connected successfully")

cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS manage")
print("STEP 5: database created")

cursor.close()
database.close()

print("STEP 6: finished")
