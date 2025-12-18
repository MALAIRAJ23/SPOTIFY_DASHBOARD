CREATE OR REPLACE VIEW country_genre_pref AS
SELECT
    country,
    genre,
    COUNT(*) AS track_count
FROM spotify_tracks
GROUP BY country, genre;
