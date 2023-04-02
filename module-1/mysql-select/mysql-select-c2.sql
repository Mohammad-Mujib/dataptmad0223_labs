-- MySQL SELECT Challange-2 solution

SELECT a.au_id AS 'AUTHOR ID',
a.au_lname AS 'LAST NAME',
a.au_fname AS 'FIRST NAME', 
COUNT(t.title) AS 'COUNT_TITLE', 
pub.pub_name AS 'PUBLISHER'
FROM authors AS a
INNER JOIN titleauthor AS ta ON a.au_id = ta.au_id 
INNER JOIN titles AS t ON ta.title_id = t.title_id
INNER JOIN publishers AS pub ON t.pub_id = pub.pub_id 
GROUP BY t.title
;