select distinct on (r.peopleid, r.sportid) 
p.id, p.name, p.height, r.result, s.name,
case
    when r.result = s.record then 'Yes'
    else 'No'
end as record
from results r
join (
    select sportid , max(result) as res
    from results
    group by sportid) as bestres
on bestres.res = r.result
left join sports s 
on s.id = r.sportid
left join people p
on p.id = r.peopleid
where r.sportid = bestres.sportid;
