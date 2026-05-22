import streamlit as st
import pandas as pd
import plotly.express as px

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

# PAGE CONFIG
st.set_page_config(
    page_title="Model Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #141E30,
        #243B55
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

.metric-box {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown(
    "<div class='main-title'>📊 Model Performance Dashboard</div>",
    unsafe_allow_html=True
)

# SUBTITLE
st.markdown(
    "<div class='sub-title'>YOLOv8 Training Analytics & AI Insights</div>",
    unsafe_allow_html=True
)

# METRICS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class='metric-box'>
            <h2>🎯 Accuracy</h2>
            <h1>94%</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class='metric-box'>
            <h2>⚡ Precision</h2>
            <h1>91%</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class='metric-box'>
            <h2>🌸 Flower Classes</h2>
            <h1>8</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# SAMPLE TRAINING DATA
data = pd.DataFrame({
    "Epoch": [1,2,3,4,5,6,7,8,9,10],
    "Accuracy": [45,52,60,68,74,81,86,90,92,94]
})

# LINE CHART
fig = px.line(
    data,
    x="Epoch",
    y="Accuracy",
    title="📈 YOLOv8 Training Accuracy"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# BAR CHART
flower_data = pd.DataFrame({
    "Flower": [
        "Rose",
        "Iris",
        "Tulip",
        "Lily",
        "Daisy"
    ],
    "Detection Accuracy": [
        95,
        94,
        90,
        88,
        91
    ]
})

fig2 = px.bar(
    flower_data,
    x="Flower",
    y="Detection Accuracy",
    title="🌿 Flower Detection Accuracy"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# FOOTER
st.markdown("---")

st.markdown(
    "<center>🤖 Real-Time AI Model Monitoring Dashboard</center>",
    unsafe_allow_html=True
)