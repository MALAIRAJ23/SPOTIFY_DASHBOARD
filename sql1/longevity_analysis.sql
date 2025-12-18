CREATE OR REPLACE VIEW song_longevity AS
SELECT
    CASE
        WHEN release_year < 2000 THEN 'Before 2000'
        WHEN release_year BETWEEN 2000 AND 2010 THEN '2000-2010'
        WHEN release_year BETWEEN 2011 AND 2020 THEN '2011-2020'
        ELSE 'After 2020'
    END AS era,
    COUNT(*) AS total_tracks,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY era;
