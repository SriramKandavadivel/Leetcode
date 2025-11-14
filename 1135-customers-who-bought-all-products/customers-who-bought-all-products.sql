# Write your MySQL query statement below
select c.customer_id 
from Customer c
-- join product p on c.customer_id = p.customer_id
group by c.customer_id
having count(distinct product_key) = (select count(*) from Product) ;