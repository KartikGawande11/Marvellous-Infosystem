'''Deep Learning Assignment

A software company is experiencing high employee turnover. Management wants to build an intelligent system that can identify employees likely to leave the company.
The HR depsutment has collected historical employee information.
Dataset

Create a CSV file named:
Employee Attrition.csV
Assignment

Yes/No-Target

Build a Deep Learning-based Employee Attrition Prediction System using MLPClassifier.
The system should accept employee information and predict

0-Employee is likely to stay
1- Employee is likely to leave

Tasks

1 Loud the dataset using Pandas

2 Display the shape, columns anal first five reconds.

3 Check for missing values 

4 Identify numerical and categorical features.

5 Convert categorical features such as Overtime into numerical representation 

6 Convert the target Attrition to and 0 and 1

7 Separate independent and dependent variables.

8 Divide the dataset into training and testing dara.

9 Apply appropriate feature scaling. 

10 Design an MLP with at least two hidden layers.

11 Train the network. 

12 Display the the number of iterations required for training.

13 Calculate training accuracy.

14 Calculate testing accuracy .

15 Generate a confusion matrix. 

16 Plot the loss curve

17 Creste a function: PredictAttrition employee data

18 Test the systers using at least five new employee reconds 

19 Explain whether the model is suffering from overfitting or undertitting.'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
Border="-"*30
print(Border)
print("1 Loud the dataset using Pandas")
print(Border)
df=pd.read_csv("Employee_Attrition.csv")
print(df)

# step 2 Display the shape, columns anal first five reconds.
print(Border)
print(" step 2 Display the shape, columns anal first five reconds.")
print(Border)
print(df.head())
print(df.info())

# step: 3 Check for missing values 
print(Border)
print("step: 3 Check for missing values ")
print(Border)
print(df.isnull().sum())

#4 Identify numerical and categorical features.
print(Border)
print("step 4 4 Identify numerical and categorical features.")
print(Border)

numeric_features = df.select_dtypes(include=['int64','float64']).columns
categorical_features = df.select_dtypes(include=['object']).columns

print("Numerical Features:")
print(numeric_features)

print("\nCategorical Features:")
print(categorical_features)



print(Border)
print("step 5 Convert categorical features such as Overtime into numerical representation")
print(" step 6 Convert the target Attrition to and 0 and 1")
print(Border)

encoder=pd.get_dummies(
    df,
    columns=["OverTime","Attrition"],
    drop_first=True,
    dtype=int 
)

encoder.rename(columns={'Attrition_Yes': 'Attrition'}, inplace=True)
encoder.rename(columns={'OverTime_Yes': 'OverTime'}, inplace=True)
print(encoder.head())
print(encoder.info())

#All the givan categorical data should be replase on  numerical such like as 0 and 1 format

# step :7 Separate independent and dependent variables.
print(Border)
print("Step:7 Separate independent and dependent variables.")
print(Border)

X=encoder.drop('Attrition',axis=1)
Y=encoder['Attrition']
print("Separate independent and dependent variables Successful!")


# step 8 Divide the dataset into training and testing dara.
print(Border)
print("Step 8: Divide the dataset into training and testing dara.")
print(Border)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.2,random_state=42)
print("dataset into training and testing Successful! ")

# step: 9 Apply appropriate feature scaling. 
print(Border)
print("step: 9 Apply appropriate feature scaling. ")
print(Border)
scaler=StandardScaler()
X_train_scaler=scaler.fit_transform(X_train)
X_test_scaler=scaler.transform(X_test)
print("Feature scaling successfully completed.")


#10 Design an MLP with at least two hidden layers.
print(Border)
print(" step:10 Design an MLP with at least two hidden layers.")
print(Border)

MLP=MLPClassifier(
    hidden_layer_sizes=(64,32),
    activation='relu',
    solver='adam',
    max_iter=500,
    random_state=42
)

print(MLP)
print("MLP model created successfully.")


#11 Train the network.
print(Border)
print("step: 11 Train the network.")
MLP.fit(X_train_scaler,Y_train)
print("MLP model training successfully completed.")

#12 Display the the number of iterations required for training.
print(Border)
print("12 Display the the number of iterations required for training.")
print(Border)

print("Number of iterations required for training:",MLP.n_iter_)

#13 Calculate training accuracy.
print(Border)
print("step 13:13 Calculate training accuracy.")
print(Border)

Y_train_pred=MLP.predict(X_train_scaler)
Y_train_accuracy=accuracy_score(Y_train,Y_train_pred)
print("Training Accuracy:",Y_train_accuracy)

#14 Calculate testing accuracy .
print(Border)
print("Step 14: Calculate testing accuracy .")
print(Border)

Y_test_pred=MLP.predict(X_test_scaler)
Y_test_accuracy=accuracy_score(Y_test,Y_test_pred)
print("Testing Accuracy:",Y_test_accuracy)

print(Border)
print("percentage directly:")
print(Border)
print("Testing Accuracy: {:.2f}%".format(Y_test_accuracy * 100))
print("Traning Accuracy: {:.2f}%".format(Y_train_accuracy * 100))

#15 Generate a confusion matrix. 
print(Border)
print(" step:15 Generate a confusion matrix. ")
print(Border)
cm=confusion_matrix(Y_test,Y_test_pred)
print("Confusion Matrix:")
print(cm)



plt.figure(figsize=(6, 4))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No', 'Yes'],
    yticklabels=['No', 'Yes']
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("MLP Confusion Matrix")
plt.show()


# Step 16: Plot the loss curve
print(Border)
print("Step 16: Plot the loss curve.")
print(Border)


plt.plot(MLP.loss_curve_)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Loss Curve")
plt.show()

# Step 17: Create a function to predict employee attrition
print(Border)
print("Step 17: Create a function PredictAttrition to predict employee attrition.")
print(Border)

def PredictAttrition(employe_data):
    
    # Convert input data into DataFrame
    employee_df = pd.DataFrame([employe_data])
    
    # Apply the same scaling used during training
    employee_scaled = scaler.transform(employee_df)
    
    # Make prediction
    prediction = MLP.predict(employee_scaled)
    
    if prediction[0] == 1:
        return "Employee is likely to leave the company."
    else:
        return "Employee is likely to stay in the company."
    
    
employe_data = [41, 2, 1102, 1, 2, 1, 94, 61,10, 5]
result = PredictAttrition(employe_data)

print("Prediction:", result)


# Step 20: Check for overfitting or underfitting
print(Border)
print("Step 20: Check whether the model is overfitting or underfitting.")
print(Border)

print("Training Accuracy:", Y_train_accuracy)
print("Testing Accuracy:", Y_test_accuracy)

difference = Y_train_accuracy - Y_test_accuracy

if difference > 0.10:
    print("The model may be suffering from overfitting.")
elif Y_train_accuracy < 0.70 and Y_test_accuracy < 0.70:
    print("The model may be suffering from underfitting.")
else:
    print("The model does not show significant overfitting or underfitting.")