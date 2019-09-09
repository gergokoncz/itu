select ID, name
from people
where ID not in(select peopleID from results);
