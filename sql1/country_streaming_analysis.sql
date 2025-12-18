CREATE OR REPLACE VIEW country_streams AS
SELECT
    country,
    SUM(stream_count) AS total_streams
FROM spotify_tracks
GROUP BY country;
