select p.id, p.name, count(distinct s.id)
from results r
left join sports s
on s.id = r.sportid
left join people p
on p.id = r.peopleid
where r.result = s.record
group by p.id
having count(distinct s.id) = (select count(distinct id)
    from sports);
