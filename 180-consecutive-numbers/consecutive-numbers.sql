# Write your MySQL query statement below
select distinct(num) as ConsecutiveNums
from Logs l
where (
    (select count(l1.id) from Logs l1 where abs(l1.id-l.id) = 1 and l.num = l1.num ) = 2
)