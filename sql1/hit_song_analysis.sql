CREATE OR REPLACE VIEW hit_songs AS
SELECT *
FROM (
    SELECT
        *,
        NTILE(10) OVER (ORDER BY popularity DESC) AS popularity_bucket
    FROM spotify_tracks
) t
WHERE popularity_bucket = 1;