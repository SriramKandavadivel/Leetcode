# Write your MySQL query statement below
select s.name from Employee s where s.id in (
    select e.managerId

    from Employee e 
    --  where
    --  Count(e.managerId) >= 5 
    group by e.managerId 
    having count(e.managerId) >= 5
);