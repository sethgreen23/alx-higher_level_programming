-- list the number of records with the same score in the table desc
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
