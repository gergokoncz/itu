drop table if exists project cascade;
drop table if exists researcher cascade;
drop table if exists article cascade;
drop table if exists journala cascade;
drop table if exists conferencea cascade;
drop table if exists staff cascade;
drop table if exists workson cascade;
drop table if exists writes cascade;
drop table if exists evaluates cascade;

create table project(
	pid serial not null,
	name varchar(50),
	primary key (pid)
);

create table researcher(
	rid serial not null,
	name varchar(50),
	primary key (rid)
);

create table article(
	aid serial not null,
	year integer not null,
	primary key (aid)
);

create table jorunala(
	aid integer references article(aid),
	journal varchar(50),
	volume integer,
);

create conferencea(
	aid integer references article(aid),
	conference varchar(50),
);

create table staff(
	sid serial,
	name varchar(50),
	aid_managed references article(aid)
)

create table workson(
);

create table writes();

create table evaluates();
