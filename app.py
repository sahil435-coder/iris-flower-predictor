import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="AI Iris Flower Monitoring System",
    page_icon="🌸",
    layout="wide"
)

# SIDEBAR
st.sidebar.title("🌸 AI Iris System")

st.sidebar.markdown("---")

st.sidebar.info(
    """
    🌿 Nature + AI Hybrid System

    🤖 YOLOv8 Computer Vision

    📊 Intelligent Flower Monitoring
    """
)

st.sidebar.markdown("---")

st.sidebar.success("✅ AI System Active")

# CUSTOM CSS
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
    font-size: 60px;
    font-weight: bold;
    text-align: center;
    color: #ffffff;
    margin-top: 50px;
}

.subtitle {
    text-align: center;
    font-size: 24px;
    color: #d9faff;
    margin-bottom: 40px;
}

.glass-card {
    background: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-top: 30px;
}

.feature-title {
    font-size: 28px;
    font-weight: bold;
    color: #00ffd5;
}

.feature-text {
    font-size: 18px;
    color: #ffffff;
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: #d9faff;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    """
    <div class='main-title'>
        🌸 AI Iris Flower Monitoring System
    </div>
    """,
    unsafe_allow_html=True
)

# SUBTITLE
st.markdown(
    """
    <div class='subtitle'>
        Nature Meets Artificial Intelligence
    </div>
    """,
    unsafe_allow_html=True
)

# HERO SECTION
col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '''
        <div class="glass-card">
            <div class="feature-title">
                🌿 Smart Flower Detection
            </div>

            <div class="feature-text">
                Detect iris flowers using YOLOv8 Computer Vision
                and real-time Artificial Intelligence.
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        '''
        <div class="glass-card">
            <div class="feature-title">
                🤖 AI Powered Monitoring
            </div>

            <div class="feature-text">
                Advanced AI analyzes flower images with
                high confidence and intelligent prediction.
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

# FEATURES SECTION
st.markdown("## 🚀 System Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:
    st.info("🌸 YOLOv8 Flower Detection")

with feature2:
    st.info("📊 Model Performance Dashboard")

with feature3:
    st.info("🧠 AI Vision Intelligence")

# ABOUT SECTION
st.markdown("## 🌿 About The System")

st.markdown(
    """
    <div class="glass-card">

    This AI-powered flower monitoring system uses:

    ✅ YOLOv8 Deep Learning  
    ✅ Computer Vision Technology  
    ✅ Streamlit Interactive Dashboard  
    ✅ Intelligent Flower Classification  
    ✅ Real-Time AI Prediction  

    The project combines Nature and Artificial Intelligence
    into one futuristic monitoring system.

    </div>
    """,
    unsafe_allow_html=True
)

# FOOTER
st.markdown("---")

st.markdown(
    """
    <div class="footer">
        🌸 Made with ❤️ using Streamlit + YOLOv8 🌸
    </div>
    """,
    unsafe_allow_html=True
)