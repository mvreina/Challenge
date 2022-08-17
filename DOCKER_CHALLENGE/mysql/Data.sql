use db; 

CREATE TABLE sales(
    fec_alta datetime NOT NULL,
	user_name varchar(255) NOT NULL,
	codigo_zip varchar(100) NOT NULL,
	credit_card_num varchar(100) NOT NULL,
	credit_card_type varchar(100) NOT NULL,
	cuenta_numero int NOT NULL,
	direccion varchar(255) NOT NULL,
	geo_latitud varchar(100) NOT NULL,
	geo_longitud varchar(100) NOT NULL,
	color_favorito varchar(100) NOT NULL,
	foto_dni varchar(255) NOT NULL,
	ip varchar(100) NOT NULL,
	auto varchar(100) NOT NULL,
	auto_modelo varchar(100) NOT NULL,
	auto_tipo varchar(100) NOT NULL,
	auto_color varchar(100) NOT NULL,
	cantidad_compras_realizadas int NOT NULL,
	avatar varchar(100) NOT NULL,
	fec_birthday date NOT NULL,
	id int not null AUTO_INCREMENT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE user(
	resposibility varchar(255) NOT NULL,
	name varchar(255) NOT NULL,
	password varchar(100) NOT NULL,
	id int not null AUTO_INCREMENT NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO user (id,name,password,resposibility)
VALUES (1,"admin","8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918","Administrator");

INSERT INTO user (id,name,password,resposibility)
VALUES (2,"user","04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb","Sales");


INSERT INTO user (id,name,password,resposibility)
VALUES (3,"autorizado","c71295494f98b295a12ceebae19ecfd12df46e8b2affc53a63e2a8c47fdda9ca","Authorized");