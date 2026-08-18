CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
    select salary from
    (
        select salary, dense_rank() over (order by salary desc) as t
        from Employee
    ) as rnk
    where t = N
    limit 1
  );
END