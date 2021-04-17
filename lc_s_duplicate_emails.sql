SELECT p.Email 
FROM Person AS p 
JOIN Person pe ON p.Email = pe.Email 
AND pe.Id != p.Id 
GROUP BY p.Email
