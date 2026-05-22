import streamlit as st
import pandas as pd
import os

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
    page_title="Admin Panel",
    page_icon="🔐",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# =========================================================
# CREATE FOLDERS
# =========================================================

if not os.path.exists("dataset"):
    os.makedirs("dataset")

if not os.path.exists("models"):
    os.makedirs("models")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b
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
    color: #cbd5e1;
    margin-bottom: 40px;
}

.login-box {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-top: 50px;
}

.glass-card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
}

.footer {
    text-align: center;
    margin-top: 50px;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOGIN FUNCTION
# =========================================================

def admin_login():

    st.markdown("""
    <div class='main-title'>
    🔐 Admin Panel
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sub-title'>
    Authorized Access Only
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("<div class='login-box'>", unsafe_allow_html=True)

        st.subheader("Admin Login")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("🚀 Login"):

            if username == "admin" and password == "admin123":

                st.session_state.admin_logged_in = True

                st.success("✅ Login Successful")

                st.rerun()

            else:

                st.error("❌ Invalid Credentials")

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# ADMIN DASHBOARD
# =========================================================

def admin_dashboard():

    # =====================================================
    # SIDEBAR
    # =====================================================

    st.sidebar.title("🔐 Admin Controls")

    st.sidebar.success("✅ Admin Active")

    st.sidebar.markdown("---")

    if st.sidebar.button("🚪 Logout"):

        st.session_state.admin_logged_in = False

        st.rerun()

    # =====================================================
    # TITLE
    # =====================================================

    st.markdown("""
    <div class='main-title'>
    ⚙️ System Admin Dashboard
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='sub-title'>
    Flower Detection Platform Management
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # SYSTEM STATUS
    # =====================================================

    st.markdown("## 📊 System Status")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🌸 Detection System Online")

    with c2:
        st.success("📦 Dataset System Active")

    with c3:
        st.success("🤖 YOLOv8 Model Active")

    # =====================================================
    # DATASET MANAGEMENT
    # =====================================================

    st.markdown("---")

    st.markdown("## 📁 Dataset Management")

    uploaded_dataset = st.file_uploader(
        "Upload CSV Dataset",
        type=["csv"]
    )

    if uploaded_dataset is not None:

        dataset_path = os.path.join(
            "dataset",
            uploaded_dataset.name
        )

        with open(dataset_path, "wb") as f:
            f.write(uploaded_dataset.getbuffer())

        st.success(f"✅ Dataset Uploaded: {uploaded_dataset.name}")

        df = pd.read_csv(dataset_path)

        # =================================================
        # DATASET INFO
        # =================================================

        st.markdown("### 📊 Dataset Information")

        d1, d2, d3 = st.columns(3)

        with d1:
            st.info(f"Rows: {df.shape[0]}")

        with d2:
            st.info(f"Columns: {df.shape[1]}")

        with d3:
            st.info(f"File: {uploaded_dataset.name}")

        # =================================================
        # DATASET PREVIEW
        # =================================================

        st.markdown("### 👀 Dataset Preview")

        st.dataframe(df.head())

        # =================================================
        # DATASET STATISTICS
        # =================================================

        st.markdown("### 📈 Dataset Statistics")

        st.dataframe(df.describe())

    # =====================================================
    # MODEL MANAGEMENT
    # =====================================================

    st.markdown("---")

    st.markdown("## 🤖 Model Management")

    # =====================================================
    # ACTIVE MODEL
    # =====================================================

    active_model = "yolov8n.pt"

    st.success(f"✅ Active Model: {active_model}")

    # =====================================================
    # MODEL UPLOAD
    # =====================================================

    uploaded_model = st.file_uploader(
        "Upload YOLO Model",
        type=["pt"]
    )

    if uploaded_model is not None:

        model_path = os.path.join(
            "models",
            uploaded_model.name
        )

        with open(model_path, "wb") as f:
            f.write(uploaded_model.getbuffer())

        st.success(
            f"✅ Model Uploaded Successfully: {uploaded_model.name}"
        )

    # =====================================================
    # AVAILABLE MODELS
    # =====================================================

    st.markdown("### 📦 Available Models")

    model_files = [
        file for file in os.listdir("models")
        if file.endswith(".pt")
    ]

    if len(model_files) > 0:

        for model_file in model_files:

            st.markdown(f"""
            <div class='glass-card'>

            <h3>🤖 {model_file}</h3>

            <p>
            YOLO Detection Model Available
            </p>

            </div>
            """, unsafe_allow_html=True)

    else:

        st.warning("⚠️ No Custom Models Uploaded Yet")

    # =====================================================
    # MODEL STATUS
    # =====================================================

    st.markdown("### 📊 Model Status")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.success("✅ Detection System Active")

    with m2:
        st.success("✅ YOLOv8 Loaded")

    with m3:
        st.success("✅ Prediction Engine Online")

    # =====================================================
    # SYSTEM INFORMATION
    # =====================================================

    st.markdown("---")

    st.markdown("## 🌿 System Information")

    st.info("""
    Admin access allows complete monitoring and management
    of the flower detection platform.
    """)

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("""
    <div class='footer'>

    🔐 Secure Flower Detection Administration Panel

    </div>
    """, unsafe_allow_html=True)

# =========================================================
# APP CONTROL
# =========================================================

if st.session_state.admin_logged_in:
    admin_dashboard()
else:
    admin_login()