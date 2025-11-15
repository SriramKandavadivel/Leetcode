# Write your MySQL query statement below
select t.id, 
    case
        when t.p_id is null then 'Root'
        when t.id not in (select p_id from Tree where p_id is not null) then 'Leaf'
        else 'Inner'
    end
    as type

from Tree t;