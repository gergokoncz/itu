-- drops for rentals schema
drop table if exists people cascade;
drop table if exists hcities cascade;
drop table if exists houses cascade;
drop table if exists rentals2 cascade;

-- drops for boats schema
drop table if exists bcities cascade;
drop table if exists boats2 cascade;

-- schema for rentals
create table people(
	id serial not null,
	name varchar(50) not null,
	primary key (id)
);

create table hcities(
	zip int not null,
	city varchar(50) not null,
	primary key (zip)
);

create table houses(
	id serial not null,
	street varchar(50) not null,
	zip integer references hcities(zip),
	primary key(id)
);

create table rentals2(
	pid integer not null references people(id),
	hid integer not null references houses(id),
	s int not null,
	primary key (pid, hid)
);

-- schema for boats
create table bcities(
	zip int not null,
	town varchar(50),
	primary key(zip)
);

create table boats2(
	bl char(2),
	bno int,
	z int references bcities(zip),
	bn varchar(50),
	ssn char(10),
	primary key(bl, bno)
);

-- populating rentals
insert into people(id, name)
select distinct pid, pn
from rentals;

insert into hcities(zip, city)
select distinct hz, hc
from rentals;

insert into houses(id, street, zip)
select distinct hid, hs, hz
from rentals;

insert into rentals2(pid, hid, s)
select pid, hid, s
from rentals;

-- populating boats

insert into bcities(zip, town)
select distinct z, t
from boats;

insert into boats2(bl, bno, z, bn, ssn)
select bl, bno, z, bn, ssn
from boats;
