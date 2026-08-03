# Write your MySQL query statement below
select f.name as Employee from Employee f
join Employee s on s.id = f.managerId
where f.salary > s.salary;