-- Removes all records with a score <= 5 in the table second_table

--  Deleting bad scores
DELETE FROM second_table
WHERE score <= 5;
