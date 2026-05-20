import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Iris Flower Monitoring System",
    page_icon="🌸",
    layout="wide"
)

# =========================================================
# SESSION
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================================================
# LOGIN PAGE
# =========================================================

def login():

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

    .login-box {
        background: rgba(255,255,255,0.1);
        padding: 40px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        margin-top: 80px;
    }

    .main-title {
        text-align: center;
        font-size: 55px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }

    .sub-title {
        text-align: center;
        font-size: 22px;
        color: #d9faff;
        margin-bottom: 40px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='main-title'>🌸 Iris Flower Classification System</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Secure AI Powered Flower Detection Platform</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        st.subheader("🔐 Login")

        username = st.text_input("Username")

        password = st.text_input("Password", type="password")

        if st.button("🚀 Login"):

            if username == "admin" and password == "admin123":

                st.session_state.logged_in = True

                st.success("✅ Login Successful")

                st.rerun()

            else:

                st.error("❌ Invalid Username or Password")

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# MAIN APP
# =========================================================

def main_app():

    # SIDEBAR
    st.sidebar.title("🌸 AI Iris System")

    st.sidebar.success("✅ System Active")

    st.sidebar.markdown("---")

    st.sidebar.info("🌿 AI Powered Monitoring")

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False

        st.rerun()

    # =====================================================
    # CSS
    # =====================================================

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

    # =====================================================
    # TITLE
    # =====================================================

    st.markdown("""
    <div class='main-title'>
    🌸 AI Iris Flower Monitoring System
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sub-title'>
    Artificial Intelligence Powered Iris Species Detection Platform
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # INTRODUCTION
    # =====================================================

    st.markdown("""
    <div class='glass-card'>

    <h2>🌿 About the System</h2>

    <p class='description-text'>

    The AI Iris Flower Monitoring System is an advanced
    Computer Vision platform developed using YOLOv8,
    Artificial Intelligence, and Streamlit.

    The system detects and analyzes Iris flower species
    through image upload and real-time webcam monitoring.

    </p>

    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # IRIS SETOSA
    # =====================================================

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
        Iris species known for its compact petals
        and vibrant appearance.

        It is commonly used in Machine Learning and
        Computer Vision classification projects.

        </div>

        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # IRIS VERSICOLOR
    # =====================================================

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:

        st.markdown("""
        <div class='glass-card'>

        <div class='species-title'>
        🌿 Iris Versicolor
        </div>

        <div class='description-text'>

        Iris Versicolor is a medium-sized Iris flower
        with elegant petals and balanced floral patterns.

        It helps improve AI model classification accuracy
        and dataset balancing.

        </div>

        </div>
        """, unsafe_allow_html=True)

    with col4:

        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
            use_container_width=True
        )

    # =====================================================
    # IRIS VIRGINICA
    # =====================================================

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

        Iris Virginica is the largest Iris species
        among the primary dataset categories.

        The AI system uses YOLOv8 Computer Vision
        algorithms to classify this species accurately.

        </div>

        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # FEATURES
    # =====================================================

    st.markdown("---")

    st.markdown("## 🚀 System Features")

    f1, f2, f3 = st.columns(3)

    with f1:
        st.success("🌸 Smart Iris Detection")

    with f2:
        st.success("🎥 Live Webcam Monitoring")

    with f3:
        st.success("📊 AI Dataset Analytics")

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("""
    <div class='footer'>

    🌿 AI + Nature + Computer Vision Intelligence 🌿

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# APP CONTROL
# =========================================================

if st.session_state.logged_in:
    main_app()
else:
    login()