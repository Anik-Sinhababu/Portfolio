import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("new.png", width=365)

with col2:
    st.title("Anik Sinhababu")
    content = """Hello!, I am Anik and I am a python programmer, and have a descent knowledge on django. I am pursuing my B-Tech Engineering in ECE department from the college Techno Main Saltlake,   
    I have worked on several projects which are listed below. """
    st.info(content)
st.subheader("Below are some of the fun apps developed by me, if you like any of these then feel free to contact me...")

col4, col5 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col4:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])