# Write your MySQL query statement below
select e.employee_id , e.name, (
    select count(e1.employee_id) from Employees e1 where e.employee_id = e1.reports_to
) as reports_count ,
( select round(avg(e2.age)) from Employees e2 where e.employee_id = e2.reports_to) as average_age
from Employees e
having reports_count != 0
order by e.employee_id;