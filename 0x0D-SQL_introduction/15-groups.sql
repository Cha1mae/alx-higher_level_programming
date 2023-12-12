-- List the num of ppl with the same score
-- This will help us understand the distribution of scores
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
