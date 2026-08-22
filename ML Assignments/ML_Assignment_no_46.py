'''Dataset contains multiple records about the customers who invest in multiple advertisement
options.
Depends on that sales feature indicates the the increased amount in there sales
This data set contains 4 features as
TV
Radi
Television
Depends on the above three features Sales feature indicates the increased sale amount.
We have to design Machine Learning application which uses Classification technique.
Design machine learning application which follows below steps as

Step 1:
Get Data
Load data from MarvellousAdvertising.csv file into python application.

Step 2:
Clean, Prepare and Manipulate data
As we want to use the above data into machine learning application we have prepare that 
in the format which is accepted by the algorithms.

Step 3:
Train Data
Now we want to train our data for that we have to select the Machine learningalgorithm.
For that we select Linear Regression algorithm from sykit learn library.
For training purpose divide the dataset into half part.
Use train method to train our dataset.

Step 4:
Test the data
Test data by passing the remaining half part of the data set.

Step 5:
Display predicted values of Linear regression algorithms as well as expected values 
which are provided by the data set'''

####################################################################################
#Step 1:Get DataLoad data from MarvellousAdvertising.csv file into python application.
#######################################################################################

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
Border="-"*30
print("Get DataLoad data from MarvellousAdvertising.csv file into python application.")
print(Border)

df=pd.read_csv("Advertising (1).csv")
print(df)

#######################################################################################
#Step 2:Clean, Prepare and Manipulate dataAs we want to use the above data into machine 
# learning application we have prepare that in the format which is accepted by the algorithms.
###########################################################################################

print(Border)
print("Clean, Prepare and Manipulate dataAs")
print(df.head())
print(Border)
##########################################################################################
print(df.tail())
print(Border)

print(Border)
print(df.info())
print(Border)

print(Border)
print("meane value of given Dataset")
print(df.describe())
print(Border)

########################################################################################
#Step 3:
#Train Data
#Now we want to train our data for that we have to select the Machine learningalgorithm.
#For that we select Linear Regression algorithm from sykit learn library.
#For training purpose divide the dataset into half part.
#Use train method to train our dataset.
#########################################################################################
print(Border)
print("Train Data")
X=df[["TV","radio","newspaper"]]
Y=df["sales"]
# Divide dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

#Creat Model
model=LinearRegression()
model.fit(X_train,Y_train)
print(Border)

########################################################################################
#Step 4:
#Test the data
#Test data by passing the remaining half part of the data set.
########################################################################################
print(Border)
print("Test the data")
print(Border)

Y_pred = model.predict(X_test)

print("Prediction value is :", Y_pred)
print("Actual Value is :", Y_test.values)

print(Border)

###########################################################################################
#Step 5:Display predicted values of Linear regression algorithms as well as
# expected values 
#which are provided by the data set
############################################################################################
print(Border)
print("Linear regression algorithms")