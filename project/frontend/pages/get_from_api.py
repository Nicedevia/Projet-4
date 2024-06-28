import streamlit as st
import requests

st.title("get information from api")

if st.button("Call"):
    response = requests.get(url = "http://127.0.0.1:8000/auth/get-from-api")
    message = response.json()['response']
    st.write(f"response from api: [{message}]")



