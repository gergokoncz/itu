-- drop all tables at the beginning so no problem with cascading afterwards

drop table if exists people cascade;
drop table if exists enemy cascade;
drop table if exists member cascade;
drop table if exists asset;
drop table if exists opponent cascade;
drop table if exists linking cascade;
drop table if exists linking_participant cascade;
drop table if exists role cascade;
drop table if exists party;
drop table if exists sponsor cascade;
drop table if exists grants cascade;

-- create people hierarchy

create table people(
    ID serial primary key not null,
    name varchar(100) not null,
    address varchar(200) not null,
    phone varchar(50) not null,
    dob date not null,
    dod date default null
);

create table enemy(
    ID integer references people(ID) primary key
);

create table member(
    ID integer references people(ID) primary key,
    start_date date not null
);

-- create assets

create table asset(
    MemberID integer references member(ID),
    name varchar not null,
    description varchar,
    primary key(MemberID, name)
);

-- opponents assignments

create table opponent(
    MemberID integer references member(ID) not null,
    EnemyID integer references enemy(ID) not null,
    start_date date not null,
    end_date date,
    primary key(MemberID, EnemyID, start_date)
);

-- create linkings

create table linking(
    ID serial primary key not null,
    name varchar not null,
    type varchar not null,
    description varchar
);

create table linking_participant(
    linkingID integer references linking(ID),
    personID integer references people(ID)
);

-- create roles

create table role(
    ID serial not null,
    title varchar not null,
    salary numeric not null,
    start_date date not null,
    end_date date not null,
    memberID integer references member(ID),
    primary key(ID, memberID)
);

-- create party 

create table party(
    ID serial primary key,
    name varchar,
    country varchar,
    observerID integer references member(ID)
);

-- create sponser

create table sponsor(
    ID serial primary key,
    name varchar,
    industry varchar,
    address varchar
);

-- define grants and their reviews

create table grants(
    memberID integer references member(ID) not null,
    sponsorID integer references sponsor(ID) not null,
    amount numeric,
    payback varchar,
    date_granted date not null,
    review_time date not null,
    reviewerID integer references member(ID) not null,
    grade integer check(grade > 0),
    check (grade < 11)
);
