import streamlit as st

st.title("Marvellous Infosystems by Chaitany Dilip Belambkar")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF Uploaded Successfully")