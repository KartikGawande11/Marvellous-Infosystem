'''A bank provides personal loans to customers. Some customers fail to repay their loans.
The bank wants to develop a Deep Learning system that predicts whether a 
new applicant has a high probability of defaulting on the loan.
This prediction will help the bank assess risk before approving loans.

Dataset

Buikt

VL-Teget
Loan Default Prediction using Multi-Layer Perceptron

Output
0-Low default risk
1-High default risk
Tasks

1. Load and understand the dataset.

2. Perform exploratory analysis.

3. Find missing values.

4. Check whether the target classes are balanced.

5. Encode categorical variables.

6. Separate X and y.

7. Split the dataset into training and testing data.

8. Explain whether stratified splitting should be used.

9. Scale the features.

10. Create an MLPClassifier.

Start with:

MLPClassifier(

)

hidden_layer_sizes=(32, 16),

activation='relu',

solver='adam'

max iter=1000,

random state=42

11. Train the model.

12. Calculate accuracy.

13. Generate the confusion matrix.

14. Generate the classification report.

15. Calculate precision, recall and Fl-score.

16. Plot training loss.

17. Test the model on new loan applicants.

Hyperparameter Experiment
Change one parameter at a time.
Experiment 1 Activation
Identity
logistic
tanh
relu
Experiment 2 Hidden Layers'''


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.metrics import recall_score,f1_score,precision_score


Border="-"*30
print(Border)
print(" step:1 Load and understand the dataset.")
print(Border)

df=pd.read_csv("Loan_Default.csv")
print(df)

#2. Perform exploratory analysis.
print(Border)
print(" Step: 2. Perform exploratory analysis.")
print(Border)

print("Print the top 5 Data on given Data set")
print(df.head())

print("print the sahpe of given Data")
print(df.shape)

print("Display the Information of the given Dataset")
print(df.info())

print("Duplicate records check")
print(df.duplicated().sum())

print("Numerical data ka statistical analysis")
print(df.describe())

#3. Find missing values.
print(Border)
print(" Step: 3 Find missing values.")
print(Border)

print(df.isnull().sum())

#4. Check whether the target classes are balanced.
print(Border)
print(" step 4. Check whether the target classes are balanced.")
print(Border)

Numerical = df.select_dtypes(include=["int64", "float64"]).columns
Catogarical=df.select_dtypes(include=["object"]).columns
print(Numerical)
print(Catogarical)

#5. Encode categorical variables.
print(Border)
print("Step:5.5. Encode categorical variables.")
print(Border)

Encoder=pd.get_dummies(
    df,
    columns=["PreviousDefault","HomeOwnership"],
    #drop_first=True,
    
    dtype=int
)
print(Encoder.head())
print(Encoder.info())

#6. Separate X and y.
print(Border)
print("Step:6  Separate X and y.")
print(Border)

'''Independent Variables (X):
Independent variables are the input features used by the machine learning model
to make a prediction. In our dataset, all columns except Default are considered 
independent variables.

Dependent Variable (Y):
The dependent variable is the target/output that we want the machine learning model
to predict. In our dataset, Default is the dependent variable.'''
X=Encoder.drop('Default',axis=1)
Y=Encoder['Default']
print("Independent Variables (X):")
print(X.columns)

print("\nDependent Variable (Y):")
print(Y.name)

#7. Split the dataset into training and testing data.
print(Border)
print("Step 7: Split the dataset into training and testing data.")
print(Border)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,train_size=0.8,random_state=42)
print("Training and testing data split successfully.")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("Y_train:", Y_train.shape)
print("Y_test:", Y_test.shape)

# Step 8 :8. Explain whether stratified splitting should be used.
#We need to decide whether the training and testing data should,
#maintain the same proportion of each target class as the original dataset.
# know we can take the 0.3
# 80% data we should Traning and 20% Data for the testing

# step : 9 . Scale the features.
print(Border)
print("Step 9: Scale the features.")
print(Border)
Scaler=StandardScaler()
X_train_scaler=Scaler.fit_transform(X_train)
X_test_scaler=Scaler.transform(X_test)
print("Feature scaling successfully completed.")

#10. Create an MLPClassifier.
print(Border)
print(" step: 10. Create an MLPClassifier.")
print(Border)
MLP=MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)
print(MLP)
print("MLP model created successfully.")

#11. Train the model.
print(Border)
print("Step 10: 11. Train the model.")
print(Border)

MLP.fit(X_train_scaler,Y_train)
print("Train the model  successfully.")

#12. Calculate accuracy.
print(Border)
print(" step: 12. Calculate accuracy.")
print(Border)


#fCalculate  traning accuracy 
Y_train_pred=MLP.predict(X_train_scaler)
Y_train_accuracyscore=accuracy_score(Y_train,Y_train_pred)
print("Training Accuracy:",Y_train_accuracyscore)

#Calculate testing accuracy
Y_test_pred=MLP.predict(X_test_scaler)
Y_test_accuracyscore=accuracy_score(Y_test,Y_test_pred)
print("Testing  Accuracy:",Y_test_accuracyscore)

print(Border)
print("percentage directly:")
print(Border)

print("Traning Accuracy: {:.2f}%".format(Y_train_accuracyscore * 100))
print("Testing Accuracy: {:.2f}%".format(Y_test_accuracyscore * 100))

#13. Generate the confusion matrix.
print(Border)
print(" step: 13. Generate the confusion matrix.")
print(Border)
cm=confusion_matrix(Y_test,Y_test_pred)
print(cm)

#Y_test = actual values
#Y_test_pred = model's predicted values

#14. Generate the classification report.
print(Border)
print("Step: 14. Generate the classification report.")
print(Border)
report=classification_report(Y_test,Y_test_pred)
print("classification report.",report)

#15. Calculate precision, recall and Fl-score.
print(Border)
print("Step 15. Calculate precision, recall and Fl-score.")
print(Border)

precision=precision_score(Y_test,Y_test_pred)
recall=recall_score(Y_test,Y_test_pred)
Fl_scores=f1_score(Y_test,Y_test_pred)

print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", Fl_scores)

#16. Plot training loss.
print(Border)
print(" step:16 Plot training loss.")
print(Border)
plt.plot(MLP.loss_curve_)
plt.show()

print(Border)
print("Step: 17. Test the model on new loan applicants.")
print(Border)

# New loan applicant
new_applicant = [[
    35,      # Age
    50000,   # Income
    200000,  # LoanAmount
    720,     # CreditScore
    8,       # EmploymentYears
    1,       # ExistingLoans
    5000,    # MonthlyDebt
    60,      # LoanTerm
    1,       # PreviousDefault_No
    0,       # PreviousDefault_Yes
    0,       # HomeOwnership_Mortgage
    1,       # HomeOwnership_Own
    0        # HomeOwnership_Rent
]]

# Scale new applicant
new_applicant_scaled = Scaler.transform(new_applicant)

# Prediction
prediction = MLP.predict(new_applicant_scaled)

print("Prediction:", prediction)

if prediction[0] == 1:
    print("Result: High default risk")
else:
    print("Result: Low default risk")