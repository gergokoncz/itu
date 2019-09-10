select id,name
from people
where id in(
    select r1.peopleID
    from results as r1 
    left join sports as s
    on(s.id = r1.sportID)
    where r1.result = s.record 
    and 1 = (select count(distinct sportid)
        from results as r2
        where r1.peopleid = r2.peopleid));
