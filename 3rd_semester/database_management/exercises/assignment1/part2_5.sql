select count(title)
from movie
where year = 1999 
and id not in(
    select movieid
    from involved
);
