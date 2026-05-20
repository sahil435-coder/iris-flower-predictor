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
        #0f2027,
        #203a43,
        #2c5364
    );
    color: white;
}

.arch-title {
    text-align: center;
    font-size: 60px;
    font-weight: bold;
    color: white;
    margin-top: 30px;
}

.arch-subtitle {
    text-align: center;
    font-size: 24px;
    color: #d9faff;
    margin-bottom: 40px;
}

.arch-card {
    background: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-bottom: 25px;
}

.arch-heading {
    font-size: 28px;
    font-weight: bold;
    color: #00ffd5;
    margin-bottom: 15px;
}

.arch-text {
    font-size: 20px;
    line-height: 1.7;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    "<div class='arch-title'>🧠 AI System Architecture</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='arch-subtitle'>Complete AI Workflow & Technology Stack</div>",
    unsafe_allow_html=True
)

# ROW 1
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="arch-card">

    <div class="arch-heading">
    🌸 Image Upload
    </div>

    <div class="arch-text">
    User uploads iris flower image through Streamlit interface.
    </div>

    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="arch-card">

    <div class="arch-heading">
    🤖 YOLOv8 Detection
    </div>

    <div class="arch-text">
    AI model processes image using computer vision algorithms.
    </div>

    </div>
    """, unsafe_allow_html=True)

# ROW 2
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="arch-card">

    <div class="arch-heading">
    📊 Prediction Analytics
    </div>

    <div class="arch-text">
    System analyzes confidence score and classification accuracy.
    </div>

    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="arch-card">

    <div class="arch-heading">
    🌿 Intelligent Monitoring
    </div>

    <div class="arch-text">
    Smart dashboard displays final flower monitoring results.
    </div>

    </div>
    """, unsafe_allow_html=True)

# TECHNOLOGY STACK
st.markdown("## ⚙️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.info("🐍 Python")

with tech2:
    st.info("🧠 YOLOv8")

with tech3:
    st.info("🎨 Streamlit")

with tech4:
    st.info("📷 OpenCV")

# WORKFLOW
st.markdown("## 🔄 AI Workflow")

st.success("""
1️⃣ Upload Flower Image  
2️⃣ Preprocess Image  
3️⃣ Run YOLOv8 Detection  
4️⃣ Analyze Flower Features  
5️⃣ Generate Prediction Result  
6️⃣ Display Intelligent Dashboard  
""")