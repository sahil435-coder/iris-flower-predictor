import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

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
    page_icon="🌸",
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
🌸 Flower Detection System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Upload Flower Images And Detect Species Instantly
</div>
""", unsafe_allow_html=True)

# =========================================================
# DESCRIPTION
# =========================================================

st.markdown("""
<div class="glass-card">

<h2>🌿 About Detection</h2>

<p style="font-size:18px; line-height:1.8;">

This module uses YOLOv8 computer vision technology
to identify and classify flower species from uploaded images.

The system performs:
<ul>
<li>🌸 Flower Detection</li>
<li>📸 Image Analysis</li>
<li>🎯 Confidence Scoring</li>
<li>📊 Real-Time Prediction Visualization</li>
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
# DETECTION
# =========================================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    # =====================================================
    # ORIGINAL IMAGE
    # =====================================================

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

    # =====================================================
    # DETECTED IMAGE
    # =====================================================

    with col2:

        st.markdown("### 🎯 Detection Result")

        st.image(
            annotated_frame,
            use_container_width=True
        )

    # =====================================================
    # RESULTS SECTION
    # =====================================================

    st.markdown("---")

    st.markdown("## 📊 Detection Results")

    boxes = results[0].boxes

    # =====================================================
    # DETECTIONS FOUND
    # =====================================================

    if len(boxes) > 0:

        st.success("🌸 Flower Detected Successfully")

        total_detections = len(boxes)

        st.info(f"📌 Total Detections: {total_detections}")

        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            flower_name = model.names[class_id]

            st.success(f"🌸 Flower Name: {flower_name}")

            st.info(f"🎯 Confidence Score: {confidence:.2f}")

            st.progress(confidence)

    # =====================================================
    # NO DETECTION
    # =====================================================

    else:

        st.error("❌ No Flower Detected")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div class="footer">

🌿 Flower Detection & Computer Vision Platform 🌿

</div>
""", unsafe_allow_html=True)