select id,name
from people
where id in(
    select r1.peopleID
    from results as r1 
    left join sports as s
    on(s.id = r1.sportID)
    where (select count(distinct sportid)
        from results as r2
        where r1.peopleid = r2.peopleid) = 1
    and r1.result = s.record);
