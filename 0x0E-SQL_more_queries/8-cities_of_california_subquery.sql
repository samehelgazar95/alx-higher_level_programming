-- Lists all the cities of California in hbtn_0d_usa

SELECT id, name
FROM cities
WHERE name = 'California'
ORDER BY id ASC;
