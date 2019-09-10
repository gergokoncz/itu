select count(fooid)
from (select i.movieid as fooid
    from involved i
    left join person p
    on p.id = i.personid
    where p.height is not null
    group by i.movieid
    having avg(p.height) > 190) as foo;
