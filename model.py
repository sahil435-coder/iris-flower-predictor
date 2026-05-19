from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Load dataset
data = load_iris()

# Convert to DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Split data
X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Logistic Regression Model
lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)

# Accuracy comparison
print("KNN Accuracy:", knn.score(X_test, y_test))
print("Logistic Regression Accuracy:", lr.score(X_test, y_test))

from sklearn.metrics import confusion_matrix

# Predictions
y_pred = knn.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n", cm)

import joblib

joblib.dump(knn, "best_model.pkl")

print("\nModel saved as best_model.pkl")