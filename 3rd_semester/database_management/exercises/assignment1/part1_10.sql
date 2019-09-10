select s.id, s.name, s.record, min(r.result)
from results r
left join sports s 
on s.id = r.sportid
left join competitions c
on c.id = r.competitionid
group by s.id
having count(distinct c.place) = (select 
    count(distinct(place)) 
    from competitions);
