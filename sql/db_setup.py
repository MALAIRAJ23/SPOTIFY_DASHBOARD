import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="@Malai18",
    auth_plugin="mysql_native_password"

)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS spotify_db")
cursor.execute("USE spotify_db")

print("✅ Database created & selected")

cursor.close()
conn.close()
