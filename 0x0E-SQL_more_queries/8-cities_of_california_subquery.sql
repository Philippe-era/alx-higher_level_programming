-- createstable 
-- selects information from tables

SELECT id, name FROM cities
-- conditions for the table
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id;
