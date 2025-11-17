# Write your MySQL query statement below
select d.name as Department, e.name as Employee , e.salary as Salary 
from Department d, Employee e
where e.departmentId = d.Id and (
    (select count(distinct salary) from Employee e1 where e1.departmentId = e.departmentId and salary > e.salary) < 3
)