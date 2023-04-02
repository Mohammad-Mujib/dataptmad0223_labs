-- MySQL SELECT Challange-3 solution

SELECT a.au_id AS 'AUTHOR ID',
a.au_lname AS 'LAST NAME',
a.au_fname AS 'FIRST NAME',
COUNT(t.title) AS 'TOTAL'
FROM authors AS a 
INNER JOIN titles AS t ON a.au_id = t.title
GROUP BY t.title
LIMIT 3 ;

-- this query gave me the four tables but without any data. 
-- and as the challenge-4 depend on the result of challenge-3, I could not continue.