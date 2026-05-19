import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

# PAGE CONFIG
st.set_page_config(
    page_title="Smart Flower Detection",
    page_icon="🌸",
    layout="wide"
)

# LOAD MODEL
model = YOLO("yolov8_model/best.pt")

# CUSTOM CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #16222A,
        #3A6073
    );
    color: white;
}

.main-title {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-top: 20px;
}

.sub-text {
    text-align: center;
    font-size: 20px;
    color: #d9faff;
    margin-bottom: 30px;
}

.result-box {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-top: 20px;
}

.webcam-box {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    """
    <div class='main-title'>
        🌸 Smart Flower Detection
    </div>
    """,
    unsafe_allow_html=True
)

# SUBTITLE
st.markdown(
    """
    <div class='sub-text'>
        YOLOv8 Powered AI Flower Detection System
    </div>
    """,
    unsafe_allow_html=True
)

# IMAGE UPLOAD SECTION
st.markdown("## 📸 Upload Flower Image")

uploaded_file = st.file_uploader(
    "Upload Flower Image",
    type=["jpg", "jpeg", "png"]
)

# IMAGE DETECTION
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

    # CONVERT IMAGE
    image_np = np.array(image)

    # YOLO PREDICTION
    results = model.predict(
        image_np,
        conf=0.25
    )

    # DETECTED IMAGE
    annotated_frame = results[0].plot()

    with col2:

        st.subheader("AI Detection Result")

        st.image(
            annotated_frame,
            use_container_width=True
        )

    # DETECTION DETAILS
    st.markdown("## 🤖 Prediction Details")

    boxes = results[0].boxes

    if len(boxes) > 0:

        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            flower_name = model.names[class_id]

            st.markdown(
                f'''
                <div class="result-box">
                    <h3>🌸 Flower: {flower_name}</h3>
                    <h4>🎯 Confidence: {confidence:.2f}</h4>
                </div>
                ''',
                unsafe_allow_html=True
            )

    else:

        st.error("No flower detected.")

# WEBCAM SECTION
st.markdown("---")

st.markdown(
    """
    <div class='webcam-box'>
        <h2>🎥 Live Webcam Flower Detection</h2>
        <p>
            Start your webcam and let YOLOv8 detect flowers
            in real-time using Artificial Intelligence.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

run_webcam = st.checkbox("Enable Live Webcam Detection")

FRAME_WINDOW = st.image([])

camera = None

if run_webcam:

    camera = cv2.VideoCapture(0)

    while run_webcam:

        success, frame = camera.read()

        if not success:
            st.error("Failed to access webcam.")
            break

        # YOLO DETECTION
        results = model.predict(frame)

        # DRAW RESULTS
        annotated_frame = results[0].plot()

        # DISPLAY FRAME
        FRAME_WINDOW.image(
            annotated_frame,
            channels="BGR",
            use_container_width=True
        )

        # STOP BUTTON
        if st.button("Stop Webcam"):
            break

    camera.release()

# FOOTER
st.markdown("---")

st.markdown(
    """
    <center>
        🌿 AI + Nature Vision Intelligence 🌿
    </center>
    """,
    unsafe_allow_html=True
)