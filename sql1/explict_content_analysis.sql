CREATE OR REPLACE VIEW explicit_analysis AS
SELECT
    explicit,
    COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY explicit;
