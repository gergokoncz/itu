select count(id)
from (select r.peopleid as id
    from results r 
    left join competitions c 
    on c.id = r.competitionid
    group by r.peopleid
    having count(distinct c.place) > 9) as foo;
