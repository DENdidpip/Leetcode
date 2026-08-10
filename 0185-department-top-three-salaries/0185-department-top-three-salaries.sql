# Write your MySQL query statement below
select Department,  Employee, Salary
from 
(select d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary, 
        dense_rank() over (partition by d.id order by e.salary desc) as t
        from Employee e
        join  Department d on d.id = e.departmentID
        )rnk

where t <= 3;