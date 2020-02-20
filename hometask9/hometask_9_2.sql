select em.first_name, em.last_name, pos.position_name, em.salary
from staff.employee em
inner join staff.pos on em.position_id = pos.id
where em.salary < 30000;

select em.first_name, em.last_name, pos.position_name, em.salary
from staff.employee em
inner join staff.pos on em.position_id = pos.id
where (
	em.salary < 30000
	and pos.position_name="designer"
);