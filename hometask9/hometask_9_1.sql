create database if not exists staff;
use staff;
create table if not exists employee(
	id int unsigned not null auto_increment primary key,
    first_name varchar(30) not null,
    last_name varchar(30) not null,
    position_id integer not null,
    salary int not null
);
create table if not exists pos(
	id int unsigned not null auto_increment primary key,
    position_name varchar(30) not null
);

insert into employee(id, first_name, last_name, position_id, salary) values (null, 'Artem', 'Dzyuba', 1, 1000000);
insert into employee(id, first_name, last_name, position_id, salary) values (null, 'Igor', 'Akinfeev', 1, 200000);
insert into employee(id, first_name, last_name, position_id, salary) values (null, 'Denis', 'Cheryshev', 1, 300000);
insert into employee(id, first_name, last_name, position_id, salary) values (null, 'Igor', 'Smolnikov', 1, 400000);
insert into employee(id, first_name, last_name, position_id, salary) values (null, 'Boris', 'Sergeev', 3, 20000);
insert into employee(id, first_name, last_name, position_id, salary) values (null, 'Sergey', 'Sergeev', 4, 29000);
insert into employee(id, first_name, last_name, position_id, salary) values (null, 'Donald', 'Trump', 5, 999999999);

insert into pos(id, position_name) values (null, 'footballer');
insert into pos(id, position_name) values (null, 'programmer');
insert into pos(id, position_name) values (null, 'intern');
insert into pos(id, position_name) values (null, 'designer');
insert into pos(id, position_name) values (null, 'big boss');