select p.id, p.name, count(s.id)
from people p
join results r on p.id = r.peopleid
join sports s on r.sportid = s.id
where r.result = s.record
group by p.id
having count(distinct s.id) > 1;
