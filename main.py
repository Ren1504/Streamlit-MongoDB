import streamlit as st
from database import mongo_connection

conn = st.experimental_connection("mongo",type = mongo_connection, database = "pets_db")

st.write(conn.list_collection())

# collection = conn.collection(pets_db)

conn.current_collection("sample")

x = conn.find()

a = [i for i in x]

name = st.text_input(
    "Enter some Name 👇"
)

place = st.text_input(
    "Enter some place 👇"
)

record = {"Name":name,"Place":place}



if st.button("Submit"):
    conn.insert(record)
    st.experimental_rerun()



st.write(a)