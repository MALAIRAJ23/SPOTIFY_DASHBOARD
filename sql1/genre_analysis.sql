CREATE OR REPLACE VIEW genre_distribution AS
SELECT
    genre,
    COUNT(*) AS track_count,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY genre;
