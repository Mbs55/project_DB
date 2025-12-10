import streamlit as st
import os
import pandas as pd
from sqlalchemy import text
st.title("home page")
con=st.connection( "mydb",type="sql")
#con.query("create table user(id integer auto increment not null primary key,name varchar(20) not null")
with con.session as s:
    s.execute(text("drop table users if exists"))
    s.execute(text("create table users(id  int  auto_increment not null primary key,name varchar(25),password varchar(25))"))
    s.execute(text("insert into users (name,password) values ('mouad','mbs123')"))
    s.commit()


query=con.query("select * from users")
st.write(query)




