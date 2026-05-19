import streamlit as st

st.title("🌸 Smart Iris AI System")

st.markdown("""
### 🚀 Welcome to the Future of Flower Intelligence

This platform uses Machine Learning and AI to:
- Predict iris species 🌸
- Analyze flower data 📊
- Provide plant knowledge 🤖
""")

st.markdown("---")

# Animation CSS
st.markdown("""
<style>
.fade-in {
    animation: fadeIn 1.5s ease-in;
}
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# SECTION 1 (Right Image)
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🌼 Iris Setosa")
    st.write("Small, simple, easy to classify.")

with col2:
    st.image("images/setosa.jpg", use_container_width=True)

st.markdown("---")

# SECTION 2 (Left Image)
col1, col2 = st.columns(2)

with col1:
    st.image("images/versicolor.jpg", use_container_width=True)

with col2:
    st.markdown("## 🌸 Iris Versicolor")
    st.write("Moderate complexity and features.")

st.markdown("---")

# SECTION 3
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 🌺 Iris Virginica")
    st.write("Largest and most complex.")

with col2:
    st.image("images/virginica.jpg", use_container_width=True)

st.markdown("---")

# SECTION 4
col1, col2 = st.columns(2)

with col1:
    st.image("images/iris4.jpg", use_container_width=True)

with col2:
    st.markdown("## 🌿 More Species")
    st.write("There are hundreds of iris species worldwide.")