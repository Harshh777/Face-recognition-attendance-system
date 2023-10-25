import streamlit as st
import cv2
import os
import time
import csv
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
names = ["Tavish Gupta","Gatik Arya"]
usernames=["tavish17","gatik4"]
file_path=Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords=pickle.load(file)
authenticator=stauth.Authenticate(names,usernames,hashed_passwords,"student_dashboard","abcdef",cookie_expiry_days=30) 
name,authentication_status,username=authenticator.login(" Student Login","main")
if authentication_status==False:
    st.error("Username/Password is incorrect")
if authentication_status==None:
     st.warning("Please enter your username and password")
if authentication_status:
    st.sidebar.title(f"Welcome {name}")
    root_dir = "/Users/tavishgupta/Desktop/AP_Project/captured_images"
    csv_file = None

    if not os.path.exists(root_dir):
        os.makedirs(root_dir, exist_ok=True)

    def main():
        st.title("ENROLL STUDENT")
        global name, regno, branch, sec,cap
        name = st.text_input("Enter Name")
        regno = st.text_input("Enter Registration Number")
        branch = st.text_input("Enter Branch")
        sec = st.text_input("Enter Section")
        branch = branch.upper()
        sec = sec.upper()
        st.text("Capture Image")
        authenticator.logout("Logout","sidebar")

        if st.button("Capture"):
            create_directories()
            cap = cv2.VideoCapture(0)
            time.sleep(1)
            capture_image()

    def create_directories():
        global csv_file
        branch_sec = branch + sec
        branch_sec_dir = os.path.join(root_dir, branch_sec)
        os.makedirs(branch_sec_dir, exist_ok=True)
        csv_file = os.path.join(branch_sec_dir, branch_sec + ".csv")
        
        if not os.path.isfile(csv_file):
            with open(csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Image Path", "Registration Number", "Name", "Class"])

    def check_duplicate_registration_number(regno):
        with open(csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                if row[1] == regno:
                    return True
        return False

    def capture_image():
        if not cap.isOpened():
            st.error("Unable to access the camera. Please make sure it is connected and not in use by another application.")
            return

        if check_duplicate_registration_number(regno):
            st.warning(f"Registration number {regno} already exists")
            cap.release()
            return

        ret, frame = cap.read()

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            st.image(frame_rgb, caption="Captured Image", use_column_width=True)
            image_path = save_image(frame)
            save_to_csv(image_path)
        else:
            st.warning("No image captured")

        cap.release()

    def save_image(image):
        image_path = os.path.join(root_dir, branch + sec, regno + ".jpg")
        cv2.imwrite(image_path, image)
        st.success(f"Image saved at {image_path}")
        return image_path

    def save_to_csv(image_path):
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([image_path, regno, name, branch + sec])

    if __name__ == "__main__":
        main()
