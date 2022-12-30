import streamlit as st

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("new.png", width=400)

with col2:
    st.title("Anik Sinhababu")
    content = """Hello!, I am Anik and I am a python programmer, and have a descent knowledge on django. 
    I am pursuing my B-Tech Engineering in ECE department from the college Techno Main Saltlake,   
    I have worked on several projects which are listed below. """
    st.info(content)

with col3:
    st.title("Contact Info")
    content = ("Email-Id:- sinhababuanik@gmail.com\nPhone-No:- 7478167687\nAddress:- Saltlake Ck-268 Bidhannagar\n"
               "     Kolkata - 700091.")
    st.info(content)

