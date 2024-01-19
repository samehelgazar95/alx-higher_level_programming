-- Lists all cities
SELECT
    cities.id,
    cities.name,
    states.name
FROM cities
JOIN states
    ON state.id = cities.state_id
ORDER BY cities.id
