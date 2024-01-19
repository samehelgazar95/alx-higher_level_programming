-- Lists all the cities of California in hbtn_0d_usa

SELECT id name
FROM cities
WHERE state_id = (SELECT id FROM states where name = 'California') 
ORDER BY id ASC;
