# Write your MySQL query statement below
select customer_id,count(*) as count_no_trans 
from Visits 
left join Transactions on Transactions.visit_id = Visits.visit_id 
where Transactions.visit_id is Null 
group by Visits.customer_id ;