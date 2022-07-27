# Student-Management-System
This repository contains  student management system made with the help of Python programming language using GUI, tkinter and pymysql.

#Create a Database and a Table

#Create a database with this name: "student_management"

create database student_management;

#Create a table "student_register" under the "student_management" database.

create table student_register(
	rollno INT(10) NOT NULL PRIMARY KEY,
	firstname VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL,
	course VARCHAR(30) NOT NULL,
	branch VARCHAR(50) NOT NULL,
	year Int(10) NOT NULL,
	gender VARCHAR(30) NOT NULL,
	address VARCHAR(30) NOT NULL,
	contact VARCHAR(15) NOT NULL,
	email VARCHAR(100) NOT NULL
);
