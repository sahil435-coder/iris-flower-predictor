import streamlit as st
import joblib
import numpy as np

model = joblib.load("best_model.pkl")

st.title("🔮 Predict Iris Flower")

sepal_length = st.slider("Sepal Length", 4.0, 8.0)
sepal_width = st.slider("Sepal Width", 2.0, 5.0)
petal_length = st.slider("Petal Length", 1.0, 7.0)
petal_width = st.slider("Petal Width", 0.1, 2.5)

if st.button("Predict"):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = model.predict(data)

    result = ["Setosa", "Versicolor", "Virginica"][pred[0]]
    st.success(f"Prediction: {result}")