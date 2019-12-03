-- 1.1
select count(g_ID)
from gGarments
where g_Price is null;

-- 1.2
select count(distinct d_ID)
from gGarments
where g_ID in(select g_ID 
from gMadeOf
where mo_Percentage > 25
and f_ID in(select distinct(f_ID) 
from gElements 
where e_Element = 'Procrastinium'));

-- 1.3 -- needs refinement
select d_ID
from gGarments
where d_ID not in(select distinct co_ID
	from gGarments
);
--select d_ID, co_ID
--from gGarments
--where d_ID is null;

--1.4
select d_ID 
from gGarments
group by d_ID
having avg(g_Price) = (
select avg(g_Price) 
from gGarments
group by d_ID
order by avg(g_Price) desc
limit 1);

--1.5
select count(*)
from (select e_Element
from gElements
where LEFT(e_Element, 1) = 'C'
group by e_Element
having count(distinct f_ID) >= 5) as foo;

--1.6
select count(g_ID)
from gGarments
where
g_ID not in(
select g_ID
from gMadeOf
group by g_ID
having sum(mo_Percentage) = 100);

--1.7
select count(*)
from (select g.d_ID
	from gGarments g
	left join gHasType h
	on(g.g_ID = h.g_ID)
	left join gTypes t
	on(h.t_ID = t.t_ID)
	where t.t_Category = 'Dress'
	group by g.d_ID
	having count(distinct t.t_ID) = (select count(distinct t_ID)
		from gTypes
		where t_Category = 'Dress')) as foo;

--1.8
