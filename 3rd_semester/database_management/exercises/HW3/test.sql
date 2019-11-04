select 'boats:bl --> bl' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bl 
	from boats t 
	group by t.bl
	 having count(distinct t.bl) > 1
	) X;

select 'boats:bl --> bno' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bl 
	from boats t 
	group by t.bl
	 having count(distinct t.bno) > 1
	) X;

select 'boats:bl --> z' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bl 
	from boats t 
	group by t.bl
	 having count(distinct t.z) > 1
	) X;

select 'boats:bl --> t' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bl 
	from boats t 
	group by t.bl
	 having count(distinct t.t) > 1
	) X;

select 'boats:bl --> bn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bl 
	from boats t 
	group by t.bl
	 having count(distinct t.bn) > 1
	) X;

select 'boats:bl --> ssn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bl 
	from boats t 
	group by t.bl
	 having count(distinct t.ssn) > 1
	) X;

select 'boats:bno --> bl' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bno 
	from boats t 
	group by t.bno
	 having count(distinct t.bl) > 1
	) X;

select 'boats:bno --> bno' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bno 
	from boats t 
	group by t.bno
	 having count(distinct t.bno) > 1
	) X;

select 'boats:bno --> z' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bno 
	from boats t 
	group by t.bno
	 having count(distinct t.z) > 1
	) X;

select 'boats:bno --> t' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bno 
	from boats t 
	group by t.bno
	 having count(distinct t.t) > 1
	) X;

select 'boats:bno --> bn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bno 
	from boats t 
	group by t.bno
	 having count(distinct t.bn) > 1
	) X;

select 'boats:bno --> ssn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bno 
	from boats t 
	group by t.bno
	 having count(distinct t.ssn) > 1
	) X;

select 'boats:z --> bl' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.z 
	from boats t 
	group by t.z
	 having count(distinct t.bl) > 1
	) X;

select 'boats:z --> bno' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.z 
	from boats t 
	group by t.z
	 having count(distinct t.bno) > 1
	) X;

select 'boats:z --> z' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.z 
	from boats t 
	group by t.z
	 having count(distinct t.z) > 1
	) X;

select 'boats:z --> t' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.z 
	from boats t 
	group by t.z
	 having count(distinct t.t) > 1
	) X;

select 'boats:z --> bn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.z 
	from boats t 
	group by t.z
	 having count(distinct t.bn) > 1
	) X;

select 'boats:z --> ssn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.z 
	from boats t 
	group by t.z
	 having count(distinct t.ssn) > 1
	) X;

select 'boats:t --> bl' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.t 
	from boats t 
	group by t.t
	 having count(distinct t.bl) > 1
	) X;

select 'boats:t --> bno' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.t 
	from boats t 
	group by t.t
	 having count(distinct t.bno) > 1
	) X;

select 'boats:t --> z' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.t 
	from boats t 
	group by t.t
	 having count(distinct t.z) > 1
	) X;

select 'boats:t --> t' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.t 
	from boats t 
	group by t.t
	 having count(distinct t.t) > 1
	) X;

select 'boats:t --> bn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.t 
	from boats t 
	group by t.t
	 having count(distinct t.bn) > 1
	) X;

select 'boats:t --> ssn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.t 
	from boats t 
	group by t.t
	 having count(distinct t.ssn) > 1
	) X;

select 'boats:bn --> bl' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bn 
	from boats t 
	group by t.bn
	 having count(distinct t.bl) > 1
	) X;

select 'boats:bn --> bno' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bn 
	from boats t 
	group by t.bn
	 having count(distinct t.bno) > 1
	) X;

select 'boats:bn --> z' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bn 
	from boats t 
	group by t.bn
	 having count(distinct t.z) > 1
	) X;

select 'boats:bn --> t' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bn 
	from boats t 
	group by t.bn
	 having count(distinct t.t) > 1
	) X;

select 'boats:bn --> bn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bn 
	from boats t 
	group by t.bn
	 having count(distinct t.bn) > 1
	) X;

select 'boats:bn --> ssn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.bn 
	from boats t 
	group by t.bn
	 having count(distinct t.ssn) > 1
	) X;

select 'boats:ssn --> bl' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.ssn 
	from boats t 
	group by t.ssn
	 having count(distinct t.bl) > 1
	) X;

select 'boats:ssn --> bno' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.ssn 
	from boats t 
	group by t.ssn
	 having count(distinct t.bno) > 1
	) X;

select 'boats:ssn --> z' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.ssn 
	from boats t 
	group by t.ssn
	 having count(distinct t.z) > 1
	) X;

select 'boats:ssn --> t' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.ssn 
	from boats t 
	group by t.ssn
	 having count(distinct t.t) > 1
	) X;

select 'boats:ssn --> bn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.ssn 
	from boats t 
	group by t.ssn
	 having count(distinct t.bn) > 1
	) X;

select 'boats:ssn --> ssn' as fd,
case when count(*) = 0 then 'may hold' 
else 'does not hold' end as validity from 
	(select t.ssn 
	from boats t 
	group by t.ssn
	 having count(distinct t.ssn) > 1
	) X;

