USE spotify_db;

-- 3. Genre distribution
SELECT
    genre,
    COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY genre
ORDER BY track_count DESC;

-- 4. Popularity trend by year
SELECT
    release_year,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY release_year
ORDER BY release_year;

-- 5. Explicit vs Non-explicit tracks
SELECT
    explicit,
    COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY explicit;

-- 6. Top countries by total streams
SELECT
    country,
    SUM(stream_count) AS total_streams
FROM spotify_tracks
GROUP BY country
ORDER BY total_streams DESC
LIMIT 10;
