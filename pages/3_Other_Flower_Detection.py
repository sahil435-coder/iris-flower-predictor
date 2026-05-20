import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# PAGE CONFIG
st.set_page_config(
    page_title="Other Flower Detection",
    page_icon="🌼",
    layout="wide"
)

# LOAD MODEL
model = YOLO("yolov8n.pt")

# CSS
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
    font-size: 50px;
    font-weight: bold;
    color: white;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #d9faff;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("""
<div class='main-title'>
🌼 Other Flower Detection
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
AI Detection for Multiple Flower Species
</div>
""", unsafe_allow_html=True)

# UPLOAD
uploaded_file = st.file_uploader(
    "Upload Flower Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            image,
            caption="Uploaded Flower",
            use_container_width=True
        )

    image_np = np.array(image)

    results = model.predict(
        image_np,
        conf=0.25
    )

    annotated_frame = results[0].plot()

    with col2:

        st.image(
            annotated_frame,
            caption="Flower Detection Result",
            use_container_width=True
        )

    boxes = results[0].boxes

    if len(boxes) > 0:

        st.success("🌼 Flower Detected Successfully")

        for box in boxes:

            class_id = int(box.cls[0])

            confidence = float(box.conf[0])

            flower_name = model.names[class_id]

            st.info(
                f"Flower: {flower_name} | Confidence: {confidence:.2f}"
            )

            st.progress(float(confidence))

    else:

        st.error("❌ No Flower Detected")

st.markdown("---")

st.success("🌼 Multi Flower AI Module Active")