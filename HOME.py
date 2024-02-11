import streamlit as st
from streamlit_lottie import st_lottie 
import json
import os

def home():
    st.header("FACE RECOGNITION ATTENDANCE SYSTEM\n")
    st.text("\n\n")
    path = "Animations/Animation - 1697706571258.json"
    if os.path.exists(path):
        with open(path,"r") as file: 
            url = json.load(file) 
        st_lottie(url, 
            reverse=True, 
            height=600, 
            width=600, 
            speed=1, 
            loop=True, 
            quality='high', 
            key='Car'
        )
    else:
        st.error("Lottie animation file not found. Please check the path.")
    st.sidebar.success("OPTIONS")

home()

