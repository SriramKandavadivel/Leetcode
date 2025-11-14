# Write your MySQL query statement below
select Date_Format(t.trans_date, '%Y-%m') as Month,t.country,count(*)  as trans_count,sum(Case when t.state = "approved" then 1 else 0 end)  as approved_count,sum(t.amount) as trans_total_amount,
    sum(case when t.state = "approved"  then t.amount else 0 end)  as approved_total_amount
from Transactions t
group by DATE_FORMAT(t.trans_date, '%Y-%m'), t.country;