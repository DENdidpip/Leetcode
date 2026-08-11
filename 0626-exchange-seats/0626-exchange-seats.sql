# Write your MySQL query statement below
select id, 
case 
when id % 2 = 1 and id < (select max(id) from Seat)
then (select student from Seat s2 where s2.id = Seat.id+1) 

when id % 2 = 0
then (select student from Seat s2 where s2.id = Seat.id-1) 

else student 
end as student

from Seat;
