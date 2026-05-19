import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

st.title("📊 Analytics")

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

fig, ax = plt.subplots()
ax.scatter(df['petal length (cm)'], df['petal width (cm)'])
st.pyplot(fig)