select count(distinct i1.personid)
from involved i1
left join movie_genre mg2
on i1.movieid = mg2.movieid
where(
    select count(distinct mg.genre)
    from involved i2
    left join movie_genre mg
    on i2.movieid = mg.movieid
    where i1.personid = i2.personid
    and mg.genre in(
        select distinct genre 
        from genre
        where category = 'Lame')
) = (
select count(distinct genre)
from genre
where category = 'Lame'
);
