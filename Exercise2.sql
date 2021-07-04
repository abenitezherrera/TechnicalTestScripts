create database test;
use test;
create table users(
user_id varchar(10) primary key not null,
country varchar(255),
username varchar(255),
gender varchar(255),
registration_date datetime);

create table job_titles(
user_id varchar(10) primary key not null,
job_title varchar(255),
standar_title varchar(255),
registration_date datetime);

create table addresses(
user_id varchar(10) primary key not null,
street_address varchar(255),
city varchar(255),
state varchar(255),
address_type varchar(45),
update_date datetime);

ALTER TABLE job_titles
DROP PRIMARY KEY,
ADD COLUMN job_id INT NOT NULL
FIRST,
ADD PRIMARY KEY (job_id);
select * from job_titles;


ALTER TABLE addresses
DROP PRIMARY KEY,
ADD COLUMN address_id INT NOT NULL
FIRST,
ADD PRIMARY KEY (address_id);
select * from addresses;

ALTER TABLE users
ADD COLUMN job_id int not null
AFTER user_id,
ADD COLUMN address_id int not null
AFTER job_id;

ALTER TABLE users 
ADD CONSTRAINT job_id_fk
FOREIGN KEY ( job_id ) REFERENCES job_titles(job_id ) ON DELETE CASCADE ON UPDATE RESTRICT,
ADD CONSTRAINT address_id_fk
FOREIGN KEY ( address_id ) REFERENCES addresses(address_id ) ON DELETE CASCADE ON UPDATE RESTRICT;
select * from users;

describe test.users;


create TABLE FINAL_TABLE(
user_id varchar(10) PRIMARY KEY not null,
country varchar(255),
job_title varchar(255),
street_address varchar(255)
);

select * from FINAL_TABLE; 

alter table job_titles drop column user_id;
insert into job_titles values('25', 'Analyst','An-ls','2015-11-05 14:29:36');
insert into job_titles values('77', 'Consultant','Co-tn','2015-11-05 14:29:36');
insert into job_titles values('33', 'Data Engineer','Da-En','2015-11-05 14:29:36');
select * from job_titles;



alter table addresses drop column user_id;
insert into addresses values('4', 'St street','Queretaro', 'Queretaro','A','2015-11-05 14:29:36');
insert into addresses values('7', 'St Johns','Guadalajara','Jalisco','A','2015-11-05 14:29:36');
insert into addresses values('6', 'St Grey','Monterrey','Nuevo Leon','C','2015-11-05 14:29:36');
select * from addresses;

insert into users values('1', '77', '7','Mexico','at3n','F','2015-11-05 14:29:36');
insert into users values('2', '25', '4','Dubai','rgt1','M','2015-11-05 14:29:36');
insert into users values('3', '33', '4','China','jju7','F','2015-11-05 14:29:36');
select * from users;

INSERT INTO FINAL_TABLE(user_id,country,job_title,street_address)
SELECT u.user_id, u.country, jt.job_title, a.street_address
FROM users u 
LEFT OUTER JOIN job_titles jt on u.job_id=jt.job_id
LEFT OUTER JOIN addresses a on u.address_id=a.address_id;
select * from FINAL_TABLE; 

describe test.FINAL_TABLE;
