create database employee_management_bd;
use employee_management_bd;
create table employee( id int primary key auto_increment,
       emp_name varchar(100),
	   age int,
	   gender varchar(20),
	   mobile varchar(15) unique,
       email varchar(100) unique,
       department varchar(100),
       designation varchar(100),
       salary decimal(10,2),
       experience int,
       joining_date date,
       status enum('Active','Resigned','On Leave'));
       
