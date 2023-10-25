import streamlit as st
import os
import identify
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
names = ["Tavish Gupta","Gatik Arya"]
usernames=["tavish17","gatik4"]
file_path=Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords=pickle.load(file)
authenticator=stauth.Authenticate(names,usernames,hashed_passwords,"student_dashboard","abcdef",cookie_expiry_days=30) 
name,authentication_status,username=authenticator.login("Teacher Login","main")
if authentication_status==False:
    st.error("Username/Password is incorrect")
if authentication_status==None:
     st.warning("Please enter your username and password")
if authentication_status:
    st.sidebar.title(f"Welcome {name}")
    st.title("TAKE ATTENDANCE")
    save_path="/Users/tavishgupta/Desktop/AP_Project/cropped_images"
    branch=st.text_input("Enter Branch")
    sec=st.text_input("Enter Section")
    branch=branch.upper()
    sec=sec.upper()
    uploaded_file = st.file_uploader("Upload The Image Of The Class", type=["jpg", "jpeg", "png","HEIC"])
    if uploaded_file:
        file_name = uploaded_file.name

        file_path = os.path.join(save_path, file_name)

        with open(file_path, "wb") as file:
            file.write(uploaded_file.read())

        st.success(f"File '{file_name}' uploaded and saved to '{file_path}'")
    branch_sec=branch+sec
    authenticator.logout("Logout","sidebar")
    if st.button("Take Attendance"):
        identify.recognize(branch_sec,save_path)