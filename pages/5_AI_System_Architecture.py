import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title="AI System Architecture",
    page_icon="🧠",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #232526,
        #414345
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

.sub-title {
    text-align: center;
    font-size: 20px;
    color: #d9faff;
    margin-bottom: 40px;
}

.arch-card {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
}

.arch-title {
    font-size: 28px;
    font-weight: bold;
    color: #00ffd5;
}

.arch-text {
    font-size: 18px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    "<div class='main-title'>🧠 AI System Architecture</div>",
    unsafe_allow_html=True
)

# SUBTITLE
st.markdown(
    "<div class='sub-title'>Complete AI Workflow & Technology Stack</div>",
    unsafe_allow_html=True
)

# FIRST ROW
col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '''
        <div class="arch-card">
            <div class="arch-title">
                🌸 Image Upload
            </div>

            <div class="arch-text">
                User uploads iris flower image
                through Streamlit interface.
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        '''
        <div class="arch-card">
            <div class="arch-title">
                🤖 YOLOv8 Detection
            </div>

            <div class="arch-text">
                AI model processes image using
                computer vision algorithms.
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

# SECOND ROW
col3, col4 = st.columns(2)

with col3:

    st.markdown(
        '''
        <div class="arch-card">
            <div class="arch-title">
                📊 Prediction Analytics
            </div>

            <div class="arch-text">
                Detection confidence and flower
                classification results are generated.
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

with col4:

    st.markdown(
        '''
        <div class="arch-card">
            <div class="arch-title">
                🌿 Intelligent Monitoring
            </div>

            <div class="arch-text">
                AI system monitors and predicts
                flower species intelligently.
            </div>
        </div>
        ''',
        unsafe_allow_html=True
    )

# TECHNOLOGY STACK
st.markdown("## ⚙️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("🐍 Python")

with tech2:
    st.success("🤖 YOLOv8")

with tech3:
    st.success("🌐 Streamlit")

with tech4:
    st.success("👁️ OpenCV")

# WORKFLOW
st.markdown("## 🔄 AI Workflow")

st.info("📸 Upload Image")
st.info("🧠 YOLOv8 Processes Image")
st.info("🌸 Flower Classification")
st.info("📊 Display Prediction")
st.info("🤖 Intelligent Monitoring")

# FOOTER
st.markdown("---")

st.markdown(
    "<center>🌿 Artificial Intelligence + Nature Monitoring System 🌿</center>",
    unsafe_allow_html=True
)