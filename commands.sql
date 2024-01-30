show databases;
create database imageDB;
use timeDB;
CREATE TABLE employee ( id INT NOT NULL , name TEXT NOT NULL , photo BLOB NOT NULL , biodata BLOB NOT NULL , PRIMARY KEY (id));
select * from employee;





show databases;
use timeDB;
show tables;
select * from t;
drop table t;

create database imageDB;
use imageDB;
create table image(id int, img blob);
alter table image modify column id INT PRIMARY KEY;
select * from image;
ALTER TABLE image MODIFY COLUMN id INT AUTO_INCREMENT NOT NULL, ADD PRIMARY KEY (id);
drop table image;
CREATE TABLE image (id INT AUTO_INCREMENT NOT NULL, img BLOB, PRIMARY KEY (id));
insert into image(img) values(load_file('/home/manojpc/Pictures/images/Pink_backed_Pelican.jpg'));
