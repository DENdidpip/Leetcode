# Write your MySQL query statement below
select distinct f.num as ConsecutiveNums
from Logs f
join Logs s on f.id = s.id+1
join Logs t on f.id = t.id+2
where f.num = s.num and t.num = f.num;