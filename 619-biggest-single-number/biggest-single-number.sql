# Write your MySQL query statement below
select max(m.num) as num
from MyNumbers m 
where 
    (select count(m1.num) from MyNumbers m1 where m1.num = m.num) = 1;
            