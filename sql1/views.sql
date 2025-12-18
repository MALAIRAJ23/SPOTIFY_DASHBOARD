USE spotify_db;

-- View: Top artists by average popularity
CREATE OR REPLACE VIEW top_artists AS
SELECT
    artist_name,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY artist_name;

-- View: Popularity trend by year
CREATE OR REPLACE VIEW yearly_trends AS
SELECT
    release_year,
    AVG(popularity) AS avg_popularity
FROM spotify_tracks
GROUP BY release_year;
