select round(
NVL(sum(
case
    when
        NVL( T.isnext-first_min ,0) = 1       
    then (1/(select count(distinct s.player_id) from Activity s)) else 0
end
),0),2) as fraction
 from
( select
        a.player_id as y,
        min(a.event_date) as first_min
    from Activity a 
    group by a.player_id) X
    inner join
    (select 
            a2.player_id as U,
            MIN(a2.event_date ) AS isnext
        from Activity a2
        where a2.event_date > (
            select 
                min(a1.event_date) as first_min
            from Activity a1
            WHERE a2.player_id = a1.player_id
        ) 
        group by a2.player_id
    )  T
    on X.y = T.U;