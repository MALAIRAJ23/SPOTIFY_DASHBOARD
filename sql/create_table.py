import mysql.connector

# 1️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="@Malai18",
    database="spotify_db",
    auth_plugin="mysql_native_password"
)

cursor = conn.cursor()

# 2️⃣ SQL query MUST be inside a string
create_table_query = """
CREATE TABLE IF NOT EXISTS spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,

    track_id VARCHAR(100),
    artist_name VARCHAR(255),

    release_date DATE,
    release_year INT,

    genre VARCHAR(100),

    duration_ms INT,
    duration_min FLOAT,

    popularity INT,
    popularity_level VARCHAR(20),

    danceability FLOAT,
    energy FLOAT,
    loudness FLOAT,
    instrumentalness FLOAT,
    tempo FLOAT,

    musical_key VARCHAR(5),
    mode INT,

    explicit BOOLEAN,
    stream_count BIGINT,
    country VARCHAR(50),
    label VARCHAR(255)
);
"""

# 3️⃣ Execute query
cursor.execute(create_table_query)
conn.commit()

print("✅ Table spotify_tracks created successfully")

# 4️⃣ Close connection
cursor.close()
conn.close()
