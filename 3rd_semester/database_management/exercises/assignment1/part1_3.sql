select p.id,p.name
from results as r left join people as p
on (r.peopleID = p.id)
where r.competitionID in(
    select id 
    from competitions 
    where extract(year from held) = 2002 
    and extract(month from held) = 6)
union
select id, name
from people
where id in(
    select peopleID 
    from results as r
    left join sports as s
    on(s.id = r.sportID)
    where s.name = 'High Jump'
    and r.result = s.record
);
