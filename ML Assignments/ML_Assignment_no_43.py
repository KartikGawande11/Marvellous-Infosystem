"""Python Programming
Machine Learning Assignment
There is one data set of wether conditions.
That dataset contains information as wether and we have to decides whether to play or not.
Data set contains the target variable as Play which indicates whether to play or not.
Consider below Marvellous Infosystems Play Predictor Dataset as
Marvellous Infosystems Play Predictor
Wether
Temperature
According to above dataset there are two features as
1. Wether
2. Temperature
We have two labels as
1. Yes
2. No
There are three types of different entries under Wether as
1. Sunny
2. Overcast
3. Rainy
There are three types of different entries under Temperature as
1. Hot
2. Cold
3. Mild
Design machine learning application which follows below steps as

Step 1:
Get Data
Load data from MarvellousInfosystems_PlayPredictor.csv file into python application.

Step 2:
Clean, Prepare and Manipulate data
As we want to use the above data into machine learning application we have
prepare that in the format which is accepted by the algorithms.
As our dataset contains two features as Wether and Temperature. We have 
to replace each string field into numeric constants by using LabelEncoder from 
processing module of sklearn.

Step 3:
Train Data
Now we want to train our data for that we have to select the Machine learning algorithm.
For that we select K Nearest Neighbour algorithm.
use fit method for training purpose. For training use whole dataset.

Step 4: Test Data
After successful training now we can test our trained data by passing some
value of wether and temperature.
As we are using KNN algorithm use value of K as 3.
After providing the values check the result and display on screen.
Result may be Yes or No.

Step 5:
Calculate Accuracy Write one function as CheckAccuracy() which calculate the accuracy of our
algorithm. For calculating the accuracy divide the dataset into two equal parts as Training 
data and Testing data.
Calculate Accuracy by changing value of K."""

# Python Programming
# Machine Learning Assignment
# Marvellous Infosystems Play Predictor

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

# --------------------------------------------------
# Step 1:
# Get Data
# --------------------------------------------------

Border = "-" * 40

print(Border)
print("Data_set MarvellousInfosystems_PlayPredictor.csv")
print(Border)

df = pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

print(df)
print(Border)


# --------------------------------------------------
# Step 2:
# Clean, Prepare and Manipulate Data
# --------------------------------------------------

print(Border)
print("Clean, Prepare and Manipulate Data")
print(Border)

print("Head Data")
print(df.head())
print(Border)

print("Tail Data")
print(df.tail())
print(Border)

print("Information of Data")
df.info()
print(Border)


# Label Encoding

print(Border)
print("Label Encoding")
print(Border)

X = df[["Wether", "Temperature"]].copy()
Y = df["Play"].copy()

Wether_encoding = LabelEncoder()
Temperature_encoding = LabelEncoder()
Play_encoding = LabelEncoder()

X["Wether"] = Wether_encoding.fit_transform(X["Wether"])
X["Temperature"] = Temperature_encoding.fit_transform(X["Temperature"])

Y = Play_encoding.fit_transform(Y)


print("Data After Encoding")
print(Border)

print("Encoding of Features (X):")
print(X)
print(Border)

print("Encoding of Target (Y):")
print(Y)
print(Border)


# Complete encoded dataset

Encoded_df = X.copy()
Encoded_df["Play"] = Y

print("Complete Data After Encoding:")
print(Encoded_df)
print(Border)


# --------------------------------------------------
# Step 3:
# Train Data
# --------------------------------------------------

print(Border)
print("Train Data")
print(Border)

# Create KNN model with K = 3

model = KNeighborsClassifier(n_neighbors=3)

# Train using whole dataset

model.fit(X, Y)

print("Model Train Successful")
print(Border)


# --------------------------------------------------
# Step 4:
# Test Data
# --------------------------------------------------

print(Border)
print("Test Data")
print(Border)

# Accept Weather from user

Wether = input("Enter your Wether (Sunny/Overcast/Rainy): ")

# Accept Temperature from user

Temperature = input("Enter your Temperature (Hot/Mild/Cold): ")


# Convert user input using LabelEncoder

try:

    Wethervalue = Wether_encoding.transform([Wether])[0]

    Temperaturevalue = Temperature_encoding.transform([Temperature])[0]

except ValueError:

    print("Invalid Wether or Temperature")
    exit()


# Create test data

TestData = pd.DataFrame(
    [[Wethervalue, Temperaturevalue]],
    columns=["Wether", "Temperature"]
)


# Prediction

Result = model.predict(TestData)


# Convert numerical result back to original label

Prediction = Play_encoding.inverse_transform(Result)


print(Border)
print("Prediction Result")
print(Border)

print("Prediction:", Prediction[0])

print(Border)


# --------------------------------------------------
# Step 5:
# Calculate Accuracy
# --------------------------------------------------

def CheckAccuracy(X, Y, K):

    # Divide dataset into two equal parts

    Mid = len(X) // 2

    # First half = Training Data

    X_train = X.iloc[:Mid]
    Y_train = Y[:Mid]

    # Second half = Testing Data

    X_test = X.iloc[Mid:]
    Y_test = Y[Mid:]


    # Create KNN model

    model = KNeighborsClassifier(n_neighbors=K)


    # Train model

    model.fit(X_train, Y_train)


    # Predict testing data

    Y_pred = model.predict(X_test)


    # Calculate correct predictions

    CorrectCount = 0

    for i in range(len(Y_test)):

        if Y_pred[i] == Y_test[i]:

            CorrectCount = CorrectCount + 1


    # Calculate accuracy

    Accuracy = (CorrectCount / len(Y_test)) * 100


    return Accuracy


# --------------------------------------------------
# Calculate Accuracy for Different K
# --------------------------------------------------

print(Border)
print("Accuracy")
print(Border)

print("Accuracy for K = 1 :", CheckAccuracy(X, Y, 1))

print("Accuracy for K = 3 :", CheckAccuracy(X, Y, 3))

print("Accuracy for K = 5 :", CheckAccuracy(X, Y, 5))

print("Accuracy for K = 7 :", CheckAccuracy(X, Y, 7))

print(Border)