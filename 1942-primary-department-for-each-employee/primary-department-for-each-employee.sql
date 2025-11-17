# Write your MySQL query statement below
select e.employee_id, e.department_id
from Employee e
where e.primary_flag = 'Y' or (
    (select count(e1.employee_id) from Employee e1 where e.employee_id = e1.employee_id) = 1
);