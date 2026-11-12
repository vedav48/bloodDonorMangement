create database blood_db_aug_2026;
use blood_db_aug_2026;
create table Donor(id int primary key auto_increment,
     Name VARCHAR(100),
     blood_group varchar(5),
     phone varchar(15) unique,
     city varchar(100),
     last_donation date);
USE blood_db_aug_2026;

