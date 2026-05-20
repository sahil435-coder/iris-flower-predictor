import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Iris Flower Monitoring System",
    page_icon="🌸",
    layout="wide"
)

# ---------------- LOGIN SESSION ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN FUNCTION ---------------- #

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
        "<div class='main-title'>🌸 AI Iris Flower Monitoring System</div>",
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

# ---------------- MAIN APP ---------------- #

def main_app():

    st.sidebar.title("🌸 AI Iris System")

    st.sidebar.success("✅ System Active")

    if st.sidebar.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.rerun()

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
        margin-top: 40px;
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
        margin-top: 20px;
    }

    .feature-title {
        font-size: 28px;
        font-weight: bold;
        color: #00ffd5;
        margin-bottom: 15px;
    }

    .feature-text {
        font-size: 18px;
        color: white;
        line-height: 1.6;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='main-title'>🌸 AI Iris Flower Monitoring System</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Nature Meets Artificial Intelligence</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="glass-card">

        <div class="feature-title">
        🌿 Smart Flower Detection
        </div>

        <div class="feature-text">
        Detect iris flowers using YOLOv8 Computer Vision and Artificial Intelligence.
        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="glass-card">

        <div class="feature-title">
        🤖 AI Powered Monitoring
        </div>

        <div class="feature-text">
        Advanced AI analyzes flower images with intelligent predictions.
        </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("## 🚀 System Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("🌸 YOLOv8 Flower Detection")

    with c2:
        st.info("📊 AI Analytics Dashboard")

    with c3:
        st.info("🧠 Intelligent Monitoring")

# ---------------- APP CONTROL ---------------- #

if st.session_state.logged_in:
    main_app()
else:
    login()