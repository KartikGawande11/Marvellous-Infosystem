'''Customer Loan Approval Using Voting Classification
A bank wants to automate its loan approval process.
The bank has historical information about customers such as:

Age
Income
Credit Score
Existing Loan
Employment Experience
Loan Amount
The target column is:
LoanApproved
where:

0→ Loan Rejected
1→ Loan Approved

The bank does not want to depend on a single Machine Learning algorithm.
Build a Voting Classifier using:

Logistic Regression
Decision Tree
K-Nearest Neighbors

1. Load the dataset.
2. Check for missing values.
3. Separate input and output variables.
4. Split the dataset into training and testing data..
5. Train Logistic Regression.
6. Train Decision Tree.
7. Train KNN.
8. Calculate the individual accuracy of all three algorithms.
9. Create a Hard Voting Classifier.
10. Calculate its accuracy.
11. Create a Soft Voting Classifier.
12. Calculate its accuracy.
13. Compare:'''


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier

def main():
    Border="-"*40
    
########################################################################
# step 1 : Load the dataset.
########################################################################
    print(Border)
    print("Load the dataset.")
    print(Border)
    
    df=pd.read_csv("Customer_Loan_Approval.csv")
    print(df)
    print(Border)
    
########################################################################
# step 2 : Check for missing values.
########################################################################
    print(Border)
    print(" Check for missing values.")
    print(Border)
    print(df.isnull().sum())
    
#######################################################################
# step 3 :  Separate input and output variables.
#######################################################################
    print(Border)
    print("Separate input and output variables.")
    print(Border)
    

    X=df[['Age','Income','CreditScore','ExistingLoan','EmploymentExperience','LoanAmount']]
    Y=df['LoanApproved']
    print(X.shape)
    print(Y.shape)
    
##########################################################################
# Step 4: Split the dataset into training and testing data..
##########################################################################
   
    print(Border)
    print("Split the dataset into training and testing data.")
    print(Border)
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
    
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)

    print("Y_train shape:", Y_train.shape)
    print("Y_test shape:", Y_test.shape)
    
##########################################################################
# Step 5:  Train Logistic Regression.
##########################################################################
    print(Border)
    print("Train Logistic Regression.")
    print(Border)
    
    model1=LogisticRegression()
    model1.fit(X_train,Y_train)
    print("Train Logistic Regression successfully.")
    
    
############################################################################
# Step 6: Train Decision Tree.
############################################################################
    print(Border)
    print("Train Decision Tree.")
    print(Border)
    model2=DecisionTreeClassifier()
    model2.fit(X_train,Y_train)
    print("Train Decision Tree successfully.")
    
#############################################################################
# Step 7: Train KNN.
#############################################################################    

    print(Border)
    print("Train KNN .")
    print(Border)
    
    model3=KNeighborsClassifier(n_neighbors=5)
    model3.fit(X_train,Y_train)
    print("Train KNN successfully.")
    
###############################################################################
# Step 8: Calculate the individual accuracy of all three algorithms.
###############################################################################
    print(Border)
    print("Calculate the individual accuracy of all three algorithms..")
    print(Border)
    Y1_pred=model1.predict(X_test)
    accuracy1=accuracy_score(Y_test,Y1_pred)
    print("Logistic Regression accuracy:",accuracy1)
    print(Border)
    Y2_pred=model2.predict(X_test)
    accuracy2=accuracy_score(Y_test,Y2_pred)
    print("Decision Tree accuracy:",accuracy2)
    print(Border)
    Y3_pred=model3.predict(X_test)
    accuracy3=accuracy_score(Y_test,Y3_pred)
    print(" KNN accuracy:",accuracy3)
    
####################################################################################
# Step 9 . Create a Hard Voting Classifier.
####################################################################################
    print(Border)
    print("Create a Hard Voting Classifier")
    print(Border)
    
    model4 = VotingClassifier(
    estimators=[
        ('Logistic Regression', model1),
        ('Decision Tree', model2),
        ('Train KNN', model3)
    ],
    voting='hard'
    )
    
    # Train Hard Voting Classifier
    model4.fit(X_train, Y_train)

    print("Hard Voting Classifier trained successfully!")

######################################################################################
# Step 10. Calculate its accuracy.
######################################################################################

    print(Border)
    print("Calculate its accuracy")
    print(Border)
    
    
    Y4_pred = model4.predict(X_test)
    accuracy4 = accuracy_score(Y_test, Y4_pred)
    print("Hard Voting Classifier accuracy:", accuracy4)
    
    
########################################################################################
# Step 11: Create a Soft Voting Classifier.
########################################################################################
    print(Border)
    print(" Create a Soft Voting Classifier.")
    print(Border)
    
    print(Border)
    print("Soft Voting Classifier")
    print(Border)


    model5 = VotingClassifier(
        estimators=[
        ('lr', model1),
        ('dt', model2),
        ('knn', model3)
    ],
    voting='soft'
    )

    model5.fit(X_train, Y_train)

    Y5_pred = model5.predict(X_test)

    accuracy5 = accuracy_score(Y_test, Y5_pred)

    print("Soft Voting Classifier accuracy:", accuracy5)
    print(Border)

if __name__=="__main__":
    main()

