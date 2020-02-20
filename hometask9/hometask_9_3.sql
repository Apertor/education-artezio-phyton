create table if not exists hierarhy(
	-- id int unsigned not null auto_increment primary key,
    employee_id int unsigned,
    boss_id int unsigned,
    foreign key (employee_id) references staff.employee(id),
    foreign key (boss_id) references staff.employee(id)
);

insert into hierarhy(employee_id, boss_id) values (1, 7);
insert into hierarhy(employee_id, boss_id) values (2, 1);
insert into hierarhy(employee_id, boss_id) values (3, 1);
insert into hierarhy(employee_id, boss_id) values (3, 2);
insert into hierarhy(employee_id, boss_id) values (4, 1);
insert into hierarhy(employee_id, boss_id) values (5, 7);
insert into hierarhy(employee_id, boss_id) values (6, 7);

select em.*, boss.first_name boss_first_name, boss.last_name boss_last_name
from (
	select em.id, em.first_name, em.last_name, pos.position_name, em.salary, h.boss_id
	from employee em
	left join hierarhy h on em.id=h.employee_id
	left join pos on em.position_id = pos.id
) em
left join employee boss on em.boss_id = boss.id
where boss.last_name = "Trump"





