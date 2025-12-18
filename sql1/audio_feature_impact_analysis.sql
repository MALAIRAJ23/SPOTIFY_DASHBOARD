CREATE OR REPLACE VIEW feature_impact AS
SELECT
    ROUND(energy,1) AS energy_bucket,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY energy_bucket
ORDER BY energy_bucket;
