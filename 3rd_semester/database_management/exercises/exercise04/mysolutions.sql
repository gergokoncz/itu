-- exercise 1

drop view if exists AllAccountRecords;

create view AllAccountRecords(
    pid,
    aid,
    adate,
    abalance,
    aover,
    rid,
    rdate,
    rtype,
    ramount,
    rbalance)
as
select  a.pid,
        a.aid,
        a.adate, 
        a.abalance, 
        a.aover, 
        r.rid,
        r.rdate,
        r.rtype,
        r.ramount,
        r.rbalance
from accounts a 
left outer join accountrecords r
on (r.aid = a.aid);

-- exercise 2

drop trigger if exists CheckBills on bills;
drop function if exists CheckBills();

create function CheckBills()
returns trigger
as 
$$ 
begin
    -- we do not delete from bills
    if (TG_OP = 'DELETE') THEN
        raise exception 'function Checkbills: cannot delete from Bills!' using errcode = '45000';
    end if;

    -- may only update bIsPaid, this checks for changes to other attributes and rejects
    if (TG_OP = 'UPDATE') THEN
        raise exception 'function Checkbills: cannot update bills, except for bIsPaid!' using errcode = '45000';
    end if;
    -- 
    if (NEW.bamount < 0) then
        raise exception 'function CheckBills: amount must be non-negative' using errcode = '45000';
    end if;

    -- check due date
    if (new.bduedate <= CURRENT_DATE) then
        raise exception 'function checkbills: date must be tomorrow or later' using errcode = '45000';
    end if;
    return new;
end;
$$
language plpgsql;

create trigger Checkbills
before insert or delete or update of bid, pid, bduedate, bamount
on bills
for each row execute procedure checkbills();
