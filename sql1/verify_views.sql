USE spotify_db;

-- List all views
SHOW FULL TABLES WHERE Table_type = 'VIEW';

-- Check top artists view
SELECT * FROM top_artists LIMIT 10;

-- Check yearly trends view
SELECT * FROM yearly_trends;
