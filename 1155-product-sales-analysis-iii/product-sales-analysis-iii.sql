# Write your MySQL query statement below
select s1.product_id, s1.year as first_year, s1.quantity, s1.price
from Sales s1
where  (
    not exists(select product_id from Sales s2 
    where s2.product_id = s1.product_id and  s1.year > s2.year)
) ;