"""2: Create a neural network model to predict loan approval.

Features:

1. Applicant income

2. Credit score

3. Loan amount

4. Existing EMI

5. Employment status

Output:

0 Loan rejected

1 Loan approved

Tasks:

1. Preprocess categorical values.

2. Apply scaling.

3. Train FNN model.

4. Evaluate model.

5. Predict approval for new applicant.

Dataset

X = [

[25000, 600, 200000, 10000, 0],

[40000, 700, 300000, 8000, 1],

[60000, 750, 500000, 12000, 1],

[20000, 550, 150000, 15000, 0],

[80000, 800, 700000, 10000, 1],

[35000, 650, 250000, 9000, 1],

[18000, 500, 100000, 12000, 0],

[90000, 850, 800000, 15000, 1],

[30000, 580, 200000, 14000, 0],

[70000, 780, 600000, 10000, 1]

y = [

0, 1, 1, 0, 1,

1, 0, 1, 0, 1

Feature Meaning

[Income, Credit Score, Loan Amount, Existing EMI, Employment St

Employment Status:

0 Not Stable Stable

1

Test Input

new_applicant = [[55000, 720, 400000, 10000, 1]]

Expected Output

Prediction: Loan Approved

"""
#====================================================================
## step1: Load or create dataset.
#====================================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,r2_score
X = [

[25000, 600, 200000, 10000, 0],

[40000, 700, 300000, 8000, 1],

[60000, 750, 500000, 12000, 1],

[20000, 550, 150000, 15000, 0],

[80000, 800, 700000, 10000, 1],

[35000, 650, 250000, 9000, 1],

[18000, 500, 100000, 12000, 0],

[90000, 850, 800000, 15000, 1],

[30000, 580, 200000, 14000, 0],

[70000, 780, 600000, 10000, 1]
]


y = [

0, 1, 1, 0, 1,

1, 0, 1, 0, 1
]

print("X Dataset:",X)
print("Y Dataset:",y)

#===================================================================
# step2: 2. Clean the dataset.
#===================================================================

df=pd.DataFrame(X)
print("Null_value :",df.isnull().sum())
print("\nCleaned Dataset:")


#------------------------------------------------------------------
# step 3. Train-Test split
#------------------------------------------------------------------

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print("\nTrain-Test split successfully!")

print("X_train:", X_train)
print("X_test:", X_test)
print("Y_train:", Y_train)
print("Y_test:", Y_test)

#------------------------------------------------------------------
#3. Apply StandardScaler.
#------------------------------------------------------------------

Scaler=StandardScaler()
X_train_scaler=Scaler.fit_transform(X_train)
X_test_scaler=Scaler.transform(X_test)
print("\nStandardScaler successfully!")


#------------------------------------------------------------------
#4. Train FNN model.
#------------------------------------------------------------------
model=MLPClassifier(
    hidden_layer_sizes=(5,),
    activation='relu',
    max_iter=2000,
    random_state=42
)
# =========================================================
# Step 5: Train the model
# =========================================================

model.fit(X_train_scaler,Y_train)
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
new_applicant = [[55000, 720, 400000, 10000, 1]]
new_applicant_scald=Scaler.transform(new_applicant)
prediction=model.predict(new_applicant_scald)
print("\nNew Customer Prediction:", prediction)

if prediction[0]==1:
    print("Loan Approved")

else:
    print("Loan Rejected")