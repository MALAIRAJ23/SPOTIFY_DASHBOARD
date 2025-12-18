-- Use database
USE spotify_db;

-- 1. Total number of tracks
SELECT COUNT(*) AS total_tracks
FROM spotify_tracks;

-- 2. Top 10 artists by average popularity
SELECT
    artist_name,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY artist_name
ORDER BY avg_popularity DESC
LIMIT 10;
