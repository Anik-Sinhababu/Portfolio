import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("MY TEAM MEMBERS")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data (1).csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images_2/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images_2/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images_2/" + row["image"])
