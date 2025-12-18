CREATE OR REPLACE VIEW explicit_performance AS
SELECT
    explicit,
    COUNT(*) AS total_tracks,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY explicit;
