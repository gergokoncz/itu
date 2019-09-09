select ID, name
from people
where ID NOT IN(SELECT peopleID from results);
