-- create database

create database books;

-- Use or select database

use books;

-- Create table in database
create table books_list(
id int not null auto_increment primary key,
nome_livro varchar(255),
autor varchar(20)
);
-- Insert Data in Database
INSERT INTO books_list (id, nome_livro, autor) 
VALUES (1, "Aprendendo SQL", "Nicolas Vogiantzis");