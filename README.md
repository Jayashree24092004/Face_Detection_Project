#  Face Detection Web App using OpenCV & Streamlit

A real-time **Face Detection Web Application** built using **OpenCV** and **Streamlit**.  
This app captures live video from your webcam and detects human faces using the **Haar Cascade Classifier** technique — a fast and lightweight computer vision approach for object detection.


##  Project Overview

This project demonstrates how to integrate **computer vision** with a **web interface** using Streamlit.  
It uses your system webcam to capture frames, processes each frame with **OpenCV’s Haar Cascade Classifier**, and displays the detected faces in real-time within a web dashboard.

---

##  Techniques Used

### 1. **OpenCV (Computer Vision)**
- Used for real-time image capture, frame-by-frame analysis, and applying face detection algorithms.
- Implements the `haarcascade_frontalface_default.xml` pre-trained model to locate faces in images.

### 2. **Haar Cascade Classifier**
- A classical **object detection algorithm** based on Haar-like features and the Viola-Jones method.
- Detects faces by scanning different regions of an image and classifying them as “face” or “non-face” using cascaded classifiers.

### 3. **Streamlit (Web Application Framework)**
- Enables building **interactive data and AI/ML web apps** with minimal code.
- Provides UI elements like buttons, sliders, and live video streaming directly in the browser.

### 4. **Real-time Processing Workflow**
- Captures webcam frames using `cv2.VideoCapture()`.
- Converts frames to grayscale for efficient processing.
- Runs face detection using `faceCascade.detectMultiScale()`.
- Draws rectangles around detected faces.
- Streams output frames live to the Streamlit frontend.

---

##  Application Workflow

1. **Start Streamlit Server**  
   When you run the app, Streamlit initializes a local web server.

2. **Webcam Access**  
   The app uses OpenCV to access your camera and continuously fetch frames.

3. **Face Detection Pipeline**  
   - Each frame is converted from RGB to Grayscale.
   - Haar Cascade Classifier scans for face-like patterns.
   - Detected faces are marked with bounding boxes.

4. **Real-time Display**  
   Streamlit updates the live video feed in your browser window, showing detected faces instantly.

5. **User Interaction**  
   You can stop/start detection anytime using app buttons or refresh the stream for a new session.

##OUTPUT##
run using:streamlit run Streamlit_cam.py
<img width="688" height="693" alt="image" src="https://github.com/user-attachments/assets/72b8af6a-ff9c-4036-8003-152b292b2a7b" />
<img width="929" height="819" alt="image" src="https://github.com/user-attachments/assets/c467a187-c29f-4ea2-bfcd-806a70eddf6c" />
<img width="580" height="219" alt="image" src="https://github.com/user-attachments/assets/10005c44-6c2d-470e-a184-86bdbd23d11b" />




