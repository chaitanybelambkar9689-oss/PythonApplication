import streamlit as st

st.title("Marvellous Infosystems by Chaitany  Belambkar")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}")