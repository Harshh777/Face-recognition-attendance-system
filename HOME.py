import streamlit as st
from streamlit_lottie import st_lottie 
import json

def home():
    st.header("FACE RECOGNITION ATTENDANCE SYSTEM\n")
    st.text("\n\n")
    path = "Animations/Animation - 1697706571258.json"
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
    st.sidebar.success("OPTIONS")
home()
