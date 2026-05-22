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
    page_title="Dataset Intelligence",
    page_icon="🌿",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #134E5E,
        #71B280
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
    color: #f0ffff;
    margin-bottom: 40px;
}

.info-card {
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
    "<div class='main-title'>🌿 Dataset Intelligence</div>",
    unsafe_allow_html=True
)

# SUBTITLE
st.markdown(
    "<div class='sub-title'>AI Dataset Analysis & Flower Insights</div>",
    unsafe_allow_html=True
)

# INFO CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '''
        <div class="info-card">
            <h2>📸 Total Images</h2>
            <h1>1200+</h1>
        </div>
        ''',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '''
        <div class="info-card">
            <h2>🌸 Flower Classes</h2>
            <h1>8</h1>
        </div>
        ''',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '''
        <div class="info-card">
            <h2>🤖 YOLO Format</h2>
            <h1>YOLOv8</h1>
        </div>
        ''',
        unsafe_allow_html=True
    )

# FLOWER DATA
flower_df = pd.DataFrame({
    "Flower": [
        "Rose",
        "Iris",
        "Tulip",
        "Lily",
        "Daisy",
        "Sunflower",
        "Lotus",
        "Jasmine"
    ],
    "Images": [
        180,
        160,
        150,
        140,
        170,
        130,
        120,
        150
    ]
})

# BAR CHART
fig = px.bar(
    flower_df,
    x="Flower",
    y="Images",
    title="🌸 Dataset Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# PIE CHART
fig2 = px.pie(
    flower_df,
    names="Flower",
    values="Images",
    title="📊 Flower Dataset Percentage"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# DATASET TABLE
st.markdown("## 📋 Dataset Information")

st.dataframe(
    flower_df,
    use_container_width=True
)

# FOOTER
st.markdown("---")

st.markdown(
    "<center>🌿 Intelligent Dataset Visualization System 🌿</center>",
    unsafe_allow_html=True
)