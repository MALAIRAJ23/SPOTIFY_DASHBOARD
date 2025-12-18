import pandas as pd
import mysql.connector
import math

# ===============================
# 1️⃣ LOAD CSV
# ===============================
df = pd.read_csv("spotify_final_cleaned.csv")
print("Rows ready:", len(df))

# ===============================
# 2️⃣ FIX / CREATE COLUMNS
# ===============================
df = df.rename(columns={'key': 'musical_key'})

df['release_date'] = pd.to_datetime(
    df['release_date'], errors='coerce'
).dt.date

df['release_year'] = pd.to_datetime(
    df['release_date'], errors='coerce'
).dt.year

df['duration_min'] = df['duration_ms'] / 60000

df['popularity_level'] = pd.cut(
    df['popularity'],
    bins=[0, 40, 70, 100],
    labels=['Low', 'Medium', 'High']
)

df['mode'] = df['mode'].map({'Major': 1, 'Minor': 0})
df['explicit'] = df['explicit'].fillna(0).astype(int)

# ===============================
# 3️⃣ FINAL COLUMN ORDER
# ===============================
df = df[
    [
        'track_id', 'artist_name',
        'release_date', 'release_year',
        'genre',
        'duration_ms', 'duration_min',
        'popularity', 'popularity_level',
        'danceability', 'energy', 'loudness',
        'instrumentalness', 'tempo',
        'musical_key', 'mode',
        'explicit', 'stream_count',
        'country', 'label'
    ]
]

# ===============================
# 4️⃣ CONVERT EVERYTHING TO PURE PYTHON TYPES
# ===============================
def clean_value(v):
    if v is None:
        return None
    if isinstance(v, float) and math.isnan(v):
        return None
    return str(v) if isinstance(v, (str,)) else v

df = df.applymap(clean_value)

# ===============================
# 5️⃣ CONNECT TO MYSQL
# ===============================
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="@Malai18",
    database="spotify_db",
    auth_plugin="mysql_native_password"
)

cursor = conn.cursor()

# ===============================
# 6️⃣ INSERT QUERY
# ===============================
insert_query = """
INSERT INTO spotify_tracks (
    track_id, artist_name,
    release_date, release_year,
    genre,
    duration_ms, duration_min,
    popularity, popularity_level,
    danceability, energy, loudness,
    instrumentalness, tempo,
    musical_key, mode,
    explicit, stream_count,
    country, label
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# ===============================
# 7️⃣ SAFE INSERT (ROW BY ROW, BATCH COMMIT)
# ===============================
count = 0
for row in df.itertuples(index=False):
    cursor.execute(insert_query, tuple(row))
    count += 1

    if count % 5000 == 0:
        conn.commit()
        print(f"Inserted {count} rows...")

conn.commit()

# ===============================
# 8️⃣ VERIFY
# ===============================
cursor.execute("SELECT COUNT(*) FROM spotify_tracks")
print("✅ Rows in DB:", cursor.fetchone()[0])

cursor.close()
conn.close()

print("🎉 DATA INSERTED SUCCESSFULLY — FINALLY DONE")
