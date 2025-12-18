import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,              # 🔥 IMPORTANT FIX
    user="root",
    password="@Malai18",
    database="malai",
    auth_plugin="mysql_native_password"
)

if conn.is_connected():
    print("✅ MySQL connected successfully!")

conn.close()
