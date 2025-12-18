CREATE OR REPLACE VIEW artist_productivity AS
SELECT
    artist_name,
    COUNT(*) AS total_tracks,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY artist_name;
