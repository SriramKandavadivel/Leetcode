select p1.person_name
from (select *,sum(weight) over(order by turn) as cum
from queue) p1
where p1.cum <= 1000 order by p1.turn Desc limit 1;