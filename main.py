import streamlit as st
from database import mongo_connection

conn = st.experimental_connection("mongo",type = mongo_connection, database = "pets_db")

st.write(conn.list_collection())

