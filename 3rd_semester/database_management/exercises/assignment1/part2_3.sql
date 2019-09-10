select count(distinct movieid)
from (select movieid, genre, count(*)
    from movie_genre
    group by movieid, genre
    having count(*) > 1) as foo;
