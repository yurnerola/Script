create database yurnerola;

use yurnerola;



create table hosts
	(
		host_id int(5) primary key auto_increment,
		host_ip varchar(15),
		host_pwd varchar(30),
		host_addr varchar(30)
	);

