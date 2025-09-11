/* Write your PL/SQL query statement below */
select 
    to_char(trans_date, 'yyyy-mm') as month,
    country, 
    count(*) as trans_count,
    count(case when state = 'approved' then 1 end) as approved_count,
    sum(amount) trans_total_amount,
    sum(case when state ='approved' then amount else 0 end) as approved_total_amount
from Transactions
group by to_char(trans_date, 'yyyy-mm') ,country;