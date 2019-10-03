-- drop all tables at the beginning so no problem with cascading afterwards

drop table if exists people cascade;
drop table if exists enemy cascade;
drop table if exists member cascade;
drop table if exists asset;
drop table if exists opponent cascade;
drop table if exists linking cascade;
drop table if exists linking_participant cascade;
drop table if exists role cascade;

-- create people hierarchy

create table people(
    ID serial primary key,
    name varchar(100),
    address varchar(200),
    phone varchar(50),
    dob date,
    dod date default null
);

create table enemy(
    ID integer references people(ID) primary key
);

create table member(
    ID integer references people(ID) primary key,
    start_date date
);

-- create assets

create table asset(
    MemberID integer references member(ID),
    name varchar,
    description varchar,
    primary key(MemberID, name)
);

-- opponents assignments

create table opponent(
    MemberID integer references member(ID),
    EnemyID integer references enemy(ID),
    start_date DATE NOT NULL,
    end_date DATE,
    primary key(MemberID, EnemyID, start_date)
);

-- create linkings

create table linking(
    ID serial primary key,
    name varchar,
    type varchar,
    description varchar
);

create table linking_participant(
    linkingID integer references linking(ID),
    personID integer references people(ID)
);

-- create roles


create table role(

)
