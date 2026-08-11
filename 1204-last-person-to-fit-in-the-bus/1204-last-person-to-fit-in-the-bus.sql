# Write your MySQL query statement below
select person_name 
from (select person_name, turn,
sum(weight) over (order by turn) as tw
from Queue
)q
where tw <= 1000
order by turn desc 
limit 1;