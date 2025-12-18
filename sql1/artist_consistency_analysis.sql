CREATE OR REPLACE VIEW artist_consistency AS
SELECT
    artist_name,
    COUNT(*) AS total_tracks,
    AVG(popularity) AS avg_popularity,
    STDDEV(popularity) AS popularity_variance
FROM spotify_tracks
GROUP BY artist_name
HAVING total_tracks >= 10;
