-- -- Lists all records of the table second_table
-- of the database hbtn_0c_0


-- Display both the score and the name (in this order)
-- With "score" >= 10, Ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
