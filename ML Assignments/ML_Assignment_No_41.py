'''Python Programming
Machine Learning Assignment
There is one data set of wine which classify 
the wines according to its contents into three classes.
Consider below Wine Dataset as
These data are the results of a chemical analysis of wines grown in the same region in Italy but derived from three different cultivars. The analysis determined the quantities of 13 constituents found in each of the three types of wines.

Wine data set contains 13 features as

1) Alcohol
2) Malic acid
3) Ash
4) Alcalinity of ash
5) Magnesium
6) Total phenols
7) Flavanoids
8) Nonflavanoid phenols
9) Proanthocyanins
10)Color intensity
11) Hue
12)OD280/OD315 of diluted wines
13)Proline
According to the above features wine can be classified as
Class 1
Class 2
Class 3
We have to design Machine Learning application which uses Classification technique.
Get Data
Train Model
Improve

Clean, Prepare & Manipulate Data
Test Data
Design machine learning application which follows below steps as
Step 1: Get Data
Step 2: Clean, Prepare and Manipulate data
Step 3: Train Data
Step 4: Test Data
Step 5: Calculate Accuracy'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
#Step 1: Get Data

Border="-"*40
print(Border)
print("Get Data")
print(Border)

df=pd.read_csv("WinePredictor.csv")
print(df)
print(Border)

#Step 2: Clean, Prepare and Manipulate data
print(Border)
print("Clean, Prepare and Manipulate data")
print(Border)

print(Border)
print(df.head())
print(Border)

print(Border)
print(df.tail())
print(Border)

print(Border)
print("Information of the Data")
print(Border)

print(df.info())
print(Border)

print(Border)
print("Find the Null value of the Data set")
print(Border)

print(df.isnull().sum())
print(Border)

print(Border)
print("Average (mean) value of columns in your dataset")
print(Border)
print(df.mean(numeric_only=True))
print(Border)

#Step 3: Train Data
print(Border)
print("Train Data")
print(Border)

# Input features
X=df[["Alcohol","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols",
      "Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity",
      "Hue","OD280/OD315 of diluted wines","Proline"]]

# Target variable
Y=df["Class"]

print(Border)
print("Train-test split")
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print(Border)

print(Border)
print("Model Train")
print(Border)
model=DecisionTreeClassifier()
model.fit(X_train,Y_train)
print("Model Train Successfully")
print(Border)

#Step 4: Test Data
print(Border)
print("Test Data")
print(Border)

Y_pred=model.predict(X_test)
print("Prediction Value is :",Y_pred)
print("Actual Value is :",Y_test.values)
print(Border)

#Step 5: Calculate Accuracy
print(Border)
print("Calculate Accuracy")
print(Border)

Accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy in percentage:",Accuracy * 100,"%")
print(Border)