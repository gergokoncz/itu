select count(fooid)
from (
    select i.movieid as fooid
    from involved i
    join movie m
    on m.id = i.movieid
    where m.year = 1999
    group by i.movieid
    having count(distinct i.role) = (
        select count(role)
        from role
        )
    ) as foo;
