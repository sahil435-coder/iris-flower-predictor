import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

# =========================================================
# HIDE ADMIN PANEL FROM SIDEBAR
# =========================================================

hide_pages = """
<style>

/* Hide last page from sidebar */
[data-testid="stSidebarNav"] ul li:last-child {
    display: none;
}

</style>
"""

st.markdown(
    hide_pages,
    unsafe_allow_html=True
)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Flower Detection",
    page_icon="🌼",
    layout="wide"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = YOLO("yolov8_model/best.pt")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f2027,
        #203a43,
        #2c5364
    );
    color: white;
}

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
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
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-top: 20px;
}

.footer {
    text-align: center;
    color: white;
    font-size: 18px;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown("""
<div class="main-title">
🌼 Flower Detection System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Detect Multiple Flower Species Using YOLOv8
</div>
""", unsafe_allow_html=True)

# =========================================================
# DESCRIPTION
# =========================================================

st.markdown("""
<div class="glass-card">

<h2>🌿 About Flower Detection</h2>

<p style="font-size:18px; line-height:1.8;">

This system detects multiple flower species
using YOLOv8 computer vision technology.

Features:
<ul>
<li>🌼 Multi Flower Detection</li>
<li>📸 Image Upload Analysis</li>
<li>🎥 Live Webcam Detection</li>
<li>🎯 Confidence Score Detection</li>
</ul>

</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# IMAGE UPLOAD
# =========================================================

st.markdown("---")

st.markdown("## 📸 Upload Flower Image")

uploaded_file = st.file_uploader(
    "Choose Flower Image",
    type=["jpg", "jpeg", "png"]
)

# =========================================================
# IMAGE DETECTION
# =========================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### 🌿 Uploaded Image")

        st.image(
            image,
            use_container_width=True
        )

    image_np = np.array(image)

    # =====================================================
    # MODEL PREDICTION
    # =====================================================

    results = model.predict(
        image_np,
        conf=0.25
    )

    annotated_frame = results[0].plot()

    with col2:

        st.markdown("### 🎯 Detection Result")

        st.image(
            annotated_frame,
            use_container_width=True
        )

    # =====================================================
    # RESULTS
    # =====================================================

    st.markdown("---")

    st.markdown("## 📊 Detection Results")

    boxes = results[0].boxes

    if len(boxes) > 0:

        st.success("🌼 Flower Detected Successfully")

        total_detections = len(boxes)

        st.info(f"📌 Total Detections: {total_detections}")

        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            flower_name = model.names[class_id]

            st.success(f"🌼 Flower Name: {flower_name}")

            st.info(f"🎯 Confidence Score: {confidence:.2f}")

            st.progress(confidence)

    else:

        st.error("❌ No Flower Detected")

# =========================================================
# WEBCAM DETECTION
# =========================================================

st.markdown("---")

st.markdown("## 🎥 Live Webcam Flower Detection")

start_camera = st.button("▶️ Start Webcam")

# SMALLER CENTERED WEBCAM
col1, col2, col3 = st.columns([1,2,1])

with col2:
    FRAME_WINDOW = st.image([])

if start_camera:

    camera = cv2.VideoCapture(0)

    stop_button = st.button("⏹️ Stop Webcam")

    while camera.isOpened():

        success, frame = camera.read()

        if not success:
            st.error("❌ Webcam Error")
            break

        # =================================================
        # MODEL PREDICTION
        # =================================================

        results = model.predict(
            frame,
            conf=0.25
        )

        annotated_frame = results[0].plot()

        # =================================================
        # SMALLER WEBCAM DISPLAY
        # =================================================

        FRAME_WINDOW.image(
            annotated_frame,
            channels="BGR",
            width=700
        )

        if stop_button:
            break

    camera.release()

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div class="footer">

🌿 Flower Detection & Computer Vision Platform 🌿

</div>
""", unsafe_allow_html=True)