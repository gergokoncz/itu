select r.sportID, s.name, to_char(r.maxres, '999D99')
from (select sportID, max(result) as maxres
    from results
    group by sportID) as r
left join sports as s
on(r.sportID = s.ID)
order by r.sportID;
