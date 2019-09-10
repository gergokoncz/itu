select r.sportID, s.name, to_char(r.mr, '999D99') as maxres
from (select sportID, max(result) as mr
    from results
    group by sportID) as r
left join sports as s
on(r.sportID = s.ID)
order by r.sportID;
