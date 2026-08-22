'''Breast Cancer Prediction

Breast cancer is one of the leading causes of death among women worldwide. 
Early detection and accurate diagnosis play a critical role in increasing survival rates.
You are given  dataset containing various medical features extracted from 
breast cancer biopsy images. Your task is to develop a machine learning model that can 
accurately predict whether a tumor is Malignant (harmful) or Benign (non-harmful) based on 
the given features.

Dataset Details
Source: Breast Cancer Wisconsin Dataset
Number of Records: 569
Number of Features: 30 (real-valued features)

Note: Use load_breast_cancer() method from sklearn to load the dataset.

Features:

Mean Radius
Mean Texture
Mean Perimeter
Mean Area
Mean Smoothness
Mean Compactness
Mean Concavity
Mean Symmetry
Worst Radius, Worst Texture,... (and other statistical measurements)

Target Variable:
0→ Malignant
1→ Benign'''

#Objectives

'''1. Load and explore the dataset.

2. Perform data preprocessing steps:
Handle missing values (if any)
Normalize or scale features

3. Perform exploratory data analysis (EDA):
Summary statistics.
Visualization of feature correlations

4. Split the dataset into training and testing sets.

5. Build a machine learning classification model to predict tumor type.

6. Evaluate the model using:
Accuracy
Confusion Matrix
Precision, Recall, F1-Score

7. Provide your observations and conclusions.
Expected Deliverables
Code File:
Data loading
Preprocessing
Model building
Evaluation'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Step 1. Load and explore the dataset.
def main():

    Border = "-" * 30

    print(Border)
    print("1. Load and explore the dataset.")
    print(Border)

    df = pd.read_csv("breast-cancer-wisconsin.csv")

    print("Data:")
    print(df)
    print(Border)


    # Step 2. Perform data preprocessing
    print("Step_2: Perform data preprocessing steps")
    print(Border)

    print("Missing values:")
    print(df.isnull().sum())
    print(Border)

    # Handle missing values
    print("Handling Missing values:")

    df = df.replace("?", np.nan)

    # Convert numeric columns to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # Fill missing values with median
    df = df.fillna(df.median(numeric_only=True))

    print("After Handling missing values:")
    print(df.isnull().sum())
    print(Border)


    # Separate features and target
    print("Separate feature and target:")
    print(Border)

    X = df.drop(["CodeNumber", "CancerType"], axis=1)
    Y = df["CancerType"]

    print("X Shape:", X.shape)
    print("Y Shape:", Y.shape)
    print(Border)


    # Step 3. EDA
    print("3. Exploratory Data Analysis")
    print(Border)

    print("Summary Statistics:")
    print(df.describe())
    print(Border)

    print("Correlation Matrix:")
    print(df.corr())
    print(Border)

    # Correlation heatmap
    plt.figure(figsize=(10, 8))

    sns.heatmap(
        df.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Feature Correlation Heatmap")
    plt.show()


    # Step 4. Split dataset
    print(Border)
    print("4. Split the dataset into training and testing sets.")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("Y_train:", Y_train.shape)
    print("Y_test :", Y_test.shape)
    print(Border)


    # Normalize / Scale Features
    scalar = MinMaxScaler()

    X_train = scalar.fit_transform(X_train)
    X_test = scalar.transform(X_test)

    print("Feature Scaling Successfully Completed")
    print(Border)


    # Step 5. Build classification model
    print("5. Build a machine learning classification model")
    print(Border)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, Y_train)

    print("Classification model trained successfully.")
    print(Border)
    
    print(Border)
    print("6. Evaluate the model using Accuracy, Confusion Matrix, Precision, Recall, F1-Score")
    print(Border)

# Predict test data
    Y_pred = model.predict(X_test)

# Accuracy
    print("Accuracy:", accuracy_score(Y_test, Y_pred))

# Confusion Matrix
    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred))

# Precision, Recall, F1-Score
    print("Classification Report:")
    print(classification_report(Y_test, Y_pred))

    print(Border)

if __name__ == "__main__":
    main()