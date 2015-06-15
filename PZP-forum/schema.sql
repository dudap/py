drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  autor varchar(20) not null,
  text text not null,
  time text not null
);
drop table if exists users;
create table users (
  id integer primary key autoincrement,
  autor varchar(20) not null,
  password text not null, 
  mail text not null,
  token text not null,
  change varchar() not null
);

