import streamlit as st
import numpy as np
import pandas as pd

st.title("🌸 Iris Flower Prediction")

st.subheader("Enter Flower Measurements")

sepal_length = st.slider("Sepal Length", 0.0, 10.0, 5.0)
sepal_width = st.slider("Sepal Width", 0.0, 10.0, 3.0)
petal_length = st.slider("Petal Length", 0.0, 10.0, 4.0)
petal_width = st.slider("Petal Width", 0.0, 10.0, 1.0)

if st.button("Predict Flower"):

    if petal_length < 2:
        flower = "Setosa"
    elif petal_length < 5:
        flower = "Versicolor"
    else:
        flower = "Virginica"

    st.success(f"Predicted Flower: {flower}")