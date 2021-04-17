SELECT e.Name AS Employee 
FROM Employee e 
JOIN Employee em 
ON e.ManagerId = em.Id 
AND e.Salary > em.Salary