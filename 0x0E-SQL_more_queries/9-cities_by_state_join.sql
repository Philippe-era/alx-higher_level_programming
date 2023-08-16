-- lists all the cities

SELECT cities.id, cities.name, states.name FROM cities
-- join key word to join the tables 
JOIN states ON cities.state_id=states.id
ORDER BY cities.id;
