CREATE OR REPLACE VIEW audio_features AS
SELECT
    energy,
    danceability,
    tempo,
    popularity
FROM spotify_tracks
WHERE energy IS NOT NULL
  AND danceability IS NOT NULL
  AND popularity IS NOT NULL;
