"""1: Create a neural network model to predict whether a customer will leave a service.

Features:

1. Age

2. Monthly charges

3. Tenure

4. Number of complaints

5. Customer support calls

X = 1

[25, 500, 12, 1, 2],

[30, 700, 24, 0, 1],

[45, 1200, 6, 5, 8],

[50, 1500, 5, 6, 10],

[28, 600, 18, 1, 1],

[35, 800, 30, 0, 0],

[48, 1400, 4, 7, 9].

[52, 1600, 3, 8, 121,

[27, 550, 20, 0, 11,

[42, 1300, 8, 4.7]

1

0, 0, 1, 1, 0,

y = [ 1 0, 1, 1, 0, 1

Output:

0 Customer will stay

1 Customer will leave

Tasks:

1. Load or create dataset.

2. Clean the dataset.

3. Apply StandardScaler.

4. Train FNN model.

5. Evaluate accuracy.

Feature Meaning

[Age, Monthly Charges, Tenure, Complaints, Support Calls]

Output Meaning

0 Customer will stay

1 Customer will leave

Test Input

new_customer [[46, 1450, 5, 6, 9]]

Expected Output

Prediction: Customer may leave"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix



X = [

[25, 500, 12, 1, 2],

[30, 700, 24, 0, 1],

[45, 1200, 6, 5, 8],

[50, 1500, 5, 6, 10],

[28, 600, 18, 1, 1],

[35, 800, 30, 0, 0],

[48, 1400, 4, 7, 9],

[52, 1600, 3, 8, 121],

[27, 550, 20, 0, 11],

[42, 1300, 8, 4, 7]

]

Y= [
    0,0,1,1,0,
    0,1,1,0,1
]

# 0 Customer will stay
# 1 Customer will leave

#------------------------------------------------------------------
# step1: Load or create dataset.
#------------------------------------------------------------------
print("X data:",X)
print("Y data:",Y)

#------------------------------------------------------------------
# step2: 2. Clean the dataset.
#------------------------------------------------------------------

df=pd.DataFrame(X)
print("Null_value :",df.isnull().sum())
print("\nCleaned Dataset:")

#------------------------------------------------------------------
#3. Train-Test split
#------------------------------------------------------------------

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print("\nTrain-Test split successfully!")

print("X_train:", X_train)
print("X_test:", X_test)
print("Y_train:", Y_train)
print("Y_test:", Y_test)

#------------------------------------------------------------------
#3. Apply StandardScaler.
#------------------------------------------------------------------
Scaler=StandardScaler()
X_train_Scaler=Scaler.fit_transform(X_train)
X_test_scaler=Scaler.transform(X_test)
print("\nStandardScaler successfully!")


#------------------------------------------------------------------
#4. Train FNN model.
#------------------------------------------------------------------

model=MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    max_iter=1000,
    random_state=42
)
# =========================================================
# Step 5: Train the model
# =========================================================

model.fit(X_train_Scaler, Y_train)
print("FNN model trained successfully!")

# =========================================================
# Step 6 : pridict the model
# =========================================================
Y_pred=model.predict(X_test_scaler)
print("Actual Value:",Y_test)
print("Pridict value:",Y_pred)

# =========================================================
# Step 7 : Calculate the Accuracy
# =========================================================

accuracy=accuracy_score(Y_test,Y_pred)
print("\nAccuracy:", accuracy)


# =========================================================
# Step 8: Predict new customer
# =========================================================

new_customer=[[46, 1450, 5, 6, 7]]
#new_customer=[[0, 0, 0, 0, 0]]

# IMPORTANT:
# Use the same scaler that was fitted on training data

new_customer_scale=Scaler.transform(new_customer)
prediction=model.predict(new_customer_scale)
print("\nNew Customer Prediction:", prediction)

if prediction[0]==1:
    print(" Customer may leave")
else:
    print("Customer may Stay")