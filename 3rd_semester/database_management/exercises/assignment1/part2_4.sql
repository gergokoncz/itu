select count(distinct(personid))
from involved
where role = 'actor' 
and movieid in(select distinct(movieid)
    from involved i
    join person p
    on p.id = i.personid
    where p.name = 'Steven Spielberg'
    and i.role = 'director');
