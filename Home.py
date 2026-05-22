import streamlit as st

# =========================================================
# HIDE ADMIN PANEL FROM SIDEBAR
# =========================================================

hide_pages = """
<style>
[data-testid="stSidebarNav"] ul li:last-child {
    display: none;
}
</style>
"""

st.markdown(hide_pages, unsafe_allow_html=True)

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Flower Monitoring System",
    page_icon="🌸",
    layout="wide"
)

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
    font-size: 60px;
    font-weight: bold;
    color: white;
    margin-top: 20px;
}

.sub-title {
    text-align: center;
    font-size: 24px;
    color: #d9faff;
    margin-bottom: 50px;
}

.glass-card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-top: 20px;
}

.description-text {
    font-size: 19px;
    line-height: 1.8;
    color: white;
}

.species-title {
    font-size: 35px;
    font-weight: bold;
    color: #00ffd5;
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    margin-top: 50px;
    font-size: 18px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌸 Flower System")

st.sidebar.success("✅ System Active")

st.sidebar.markdown("---")

st.sidebar.info("🌿 Flower Monitoring Platform")

# =========================================================
# TITLE
# =========================================================

st.markdown("""
<div class='main-title'>
🌸 Flower Monitoring System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sub-title'>
Flower Classification & Detection Platform
</div>
""", unsafe_allow_html=True)

# =========================================================
# INTRODUCTION
# =========================================================

st.markdown("""
<div class='glass-card'>

<h2>🌿 About Flower Monitoring</h2>

<p class='description-text'>

The Flower Monitoring System is a modern
computer vision platform developed using
YOLOv8 and Streamlit.

The system detects and analyzes flower species
through image upload and real-time webcam monitoring.

</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# FLOWER SECTION 1
# =========================================================

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/a/a7/Irissetosa1.jpg",
        use_container_width=True
    )

with col2:

    st.markdown("""
    <div class='glass-card'>

    <div class='species-title'>
    🌸 Iris Setosa
    </div>

    <div class='description-text'>

    Iris Setosa is one of the most recognizable
    flower species known for its compact petals
    and vibrant appearance.

    It is widely used in classification and
    computer vision projects.

    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FLOWER SECTION 2
# =========================================================

st.markdown("---")

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
    <div class='glass-card'>

    <div class='species-title'>
    🌿 Iris Versicolor
    </div>

    <div class='description-text'>

    Iris Versicolor is a medium-sized flower
    with elegant petals and balanced floral patterns.

    It helps improve classification accuracy
    and dataset balancing.

    </div>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
        use_container_width=True
    )

# =========================================================
# FLOWER SECTION 3
# =========================================================

st.markdown("---")

col5, col6 = st.columns(2)

with col5:

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg",
        use_container_width=True
    )

with col6:

    st.markdown("""
    <div class='glass-card'>

    <div class='species-title'>
    🌺 Iris Virginica
    </div>

    <div class='description-text'>

    Iris Virginica is among the largest flower species
    within the primary dataset categories.

    The system uses YOLOv8 computer vision
    algorithms to classify this species accurately.

    </div>

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# FEATURES
# =========================================================

st.markdown("---")

st.markdown("## 🚀 System Features")

f1, f2, f3 = st.columns(3)

with f1:
    st.success("🌸 Smart Flower Detection")

with f2:
    st.success("🎥 Live Webcam Monitoring")

with f3:
    st.success("📊 Dataset Analytics")

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class='footer'>

🌿 Flower Detection & Monitoring Platform 🌿

</div>
""", unsafe_allow_html=True)