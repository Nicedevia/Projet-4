import streamlit as st
import requests, json

st.title("send information to api")
user_input = st.text_input("What to send to the server?")
if st.button("Send"):
    response = requests.post(
        url = "http://127.0.0.1:8000/auth/send-to-api",
        data = json.dumps(user_input)
    )
    message = response.json()['response']
    st.write(f"response from api: [{message}]")



