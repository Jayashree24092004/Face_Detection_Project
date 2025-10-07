import streamlit as st
import streamlit.components.v1 as components
import cv2
import logging as log
import datetime as dt
from time import sleep

# ---------------- Setup ---------------- #
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
log.basicConfig(filename='webcam.log', level=log.INFO)

st.title("Face Detection Through OpenCV Using Streamlit")
st.header("Streamlit")

components.html(
    "<html><body><h3>Streamlit is an open-source Python library that makes it easy to "
    "create and share beautiful, custom web apps for machine learning and data science.</h3></body></html>",
    width=700,
    height=100
)

# Sidebar inputs
st.sidebar.subheader("Details of the person")
t1 = st.sidebar.text_input("Name of Person 1")
s1 = st.sidebar.slider("Age of Person 1", 0, 100, 25)
st.sidebar.markdown("---")
t2 = st.sidebar.text_input("Name of Person 2")
s2 = st.sidebar.slider("Age of Person 2", 0, 100, 25)

st.write("Name 1:", t1, " | Age:", s1)
st.write("Name 2:", t2, " | Age:", s2)

st.header("OpenCV - Detection of Faces")
st.write("Press the button below to start face detection using your webcam.")

# ---------------- Streamlit Face Detection ---------------- #
if st.button("Start Face Detection"):
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        st.error("Unable to access webcam.")
    else:
        st.success("Webcam loaded successfully. Click Stop to end.")
        frame_window = st.image([])  # Live frame display window
        stop_button = st.button("Stop Detection")

        anterior = 0

        while True:
            ret, frame = video_capture.read()
            if not ret:
                st.error("Failed to capture frame from camera.")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if anterior != len(faces):
                anterior = len(faces)
                log.info(f"faces: {len(faces)} at {dt.datetime.now()}")

            # Convert BGR → RGB for Streamlit display
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_window.image(frame_rgb)

            # Allow user to stop
            if stop_button:
                break

        video_capture.release()
        st.info("Face detection stopped.")
