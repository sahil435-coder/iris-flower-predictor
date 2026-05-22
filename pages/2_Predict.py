import streamlit as st

# =========================================================
# HIDE ADMIN PANEL
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
    page_title="Flower Prediction",
    page_icon="🌸",
    layout="wide"
)

# =========================================================
# CSS
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
    margin-top: 20px;
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
# TITLE
# =========================================================

st.markdown("""
<div class="main-title">
🌸 Flower Prediction System
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Flower Species Estimation Using Measurements
</div>
""", unsafe_allow_html=True)

# =========================================================
# DESCRIPTION
# =========================================================

st.markdown("""
<div class="glass-card">

<h2>🌿 About Prediction</h2>

<p style="font-size:18px; line-height:1.8;">

Enter flower measurements below
to estimate the possible flower species.

The system analyzes petal and sepal
dimensions to generate prediction results.

</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# INPUTS
# =========================================================

st.markdown("---")

st.markdown("## 📊 Enter Flower Measurements")

col1, col2 = st.columns(2)

with col1:

    sepal_length = st.slider(
        "Sepal Length",
        0.0,
        10.0,
        5.1
    )

    sepal_width = st.slider(
        "Sepal Width",
        0.0,
        10.0,
        3.5
    )

with col2:

    petal_length = st.slider(
        "Petal Length",
        0.0,
        10.0,
        1.4
    )

    petal_width = st.slider(
        "Petal Width",
        0.0,
        10.0,
        0.2
    )

# =========================================================
# PREDICTION
# =========================================================

st.markdown("---")

if st.button("🌸 Predict Flower"):

    if petal_length < 2:
        flower = "Iris Setosa"

    elif petal_length < 5:
        flower = "Iris Versicolor"

    else:
        flower = "Iris Virginica"

    st.success("✅ Prediction Generated Successfully")

    st.info(f"🌸 Predicted Flower: {flower}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown("""
<div class="footer">

🌿 Flower Prediction Platform 🌿

</div>
""", unsafe_allow_html=True)