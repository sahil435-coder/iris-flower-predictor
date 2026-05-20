import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Iris Flower Detection",
    page_icon="🌸",
    layout="wide"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = YOLO("yolov8n.pt")

# =========================================================
# CUSTOM CSS
# =========================================================

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
    font-size: 55px;
    font-weight: bold;
    text-align: center;
    color: white;
    margin-top: 20px;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #d9faff;
    margin-bottom: 40px;
}

.glass-card {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-top: 20px;
}

.result-box {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: white;
    font-size: 18px;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown("""
<div class='main-title'>
🌸 Iris Flower Detection
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>

</div>
""", unsafe_allow_html=True)

# =========================================================
# DESCRIPTION
# =========================================================

st.markdown("""
<div class='glass-card'>

<h2>🌿 About Iris Detection</h2>

<p>

This module uses Artificial Intelligence and YOLOv8
Computer Vision algorithms to detect Iris flower
species from uploaded images and live webcam streams.

The system performs intelligent object detection,
flower classification, and real-time prediction
visualization.

</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# IMAGE UPLOAD
# =========================================================

st.markdown("---")

st.markdown("## 📸 Upload Iris Flower Image")

uploaded_file = st.file_uploader(
    "Upload Iris Flower",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            image,
            caption="Uploaded Iris Image",
            use_container_width=True
        )

    image_np = np.array(image)

    # AI PREDICTION
    results = model.predict(
        image_np,
        conf=0.25
    )

    annotated_frame = results[0].plot()

    with col2:

        st.image(
            annotated_frame,
            caption="AI Detection Result",
            use_container_width=True
        )

    # DETECTION RESULTS
    st.markdown("## 🤖 Detection Results")

    boxes = results[0].boxes

    if len(boxes) > 0:

        st.success("🌸 Iris Flower Detected Successfully")

        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            flower_name = model.names[class_id]

            st.markdown(
                f"""
                <div class='result-box'>
                    <h3>🌸 Flower: {flower_name}</h3>
                    <h4>🎯 Confidence: {confidence:.2f}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.progress(float(confidence))

    else:

        st.error("❌ No Iris Flower Detected")

# =========================================================
# WEBCAM DETECTION
# =========================================================

st.markdown("---")

st.markdown("## 🎥 Live Iris Webcam Detection")

start_webcam = st.button("▶️ Start Webcam")

FRAME_WINDOW = st.image([])

if start_webcam:

    camera = cv2.VideoCapture(0)

    while camera.isOpened():

        success, frame = camera.read()

        if not success:
            break

        results = model.predict(frame)

        annotated_frame = results[0].plot()

        FRAME_WINDOW.image(
            annotated_frame,
            channels="BGR",
            use_container_width=True
        )

    camera.release()

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div class='footer'>

🌿 AI + Computer Vision Iris Intelligence 🌿

</div>
""", unsafe_allow_html=True)