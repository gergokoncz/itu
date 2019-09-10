select count(fooid)
from (
    select i1.personid as fooid
    from involved i1
    join involved i2
    on i1.movieid = i2.movieid
    where i1.personid = i2.personid
    and i1.role <> i2.role
    group by i1.personid
    having count(i1.movieid) > 2) as foo;
