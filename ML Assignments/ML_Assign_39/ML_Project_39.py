"""Machine Learning

Dataset Description - Student Performance ML Dataset

The dataset student performance_ml.csv contains academic and behavioral information of 
students. The objective of this dataset is to predict whether a student will
Pass (1) or Fail (0) based on various input features.

Each row in the dataset represents one student, and each column represents a
measurable factor that may influence academic performance.
Features Description
StudyHours - Number of hours a student studies per day.
Attendance - Percentage of class attendance.
PreviousScore - Marks obtained in the previous examination.
AssignmentsCompleted - Number of assignments completed by the student.
SleepHours - Average number of hours the student sleeps per day.
FinalResult - Target variable (Output):
1→ Pass
0→ Fail
Objective of the Dataset
The goal is to:
Analyze how different factors affect student performance.
Build a Machine Learning model to predict whether a student will pass or fail.
Understand concepts such as training, testing, accuracy, confusion matrix, overfitting, 
and model evaluation
1.Import Decision Tree Classifier from sklearn. Create a model object and train it using fit().
2. Use the trained model to predict results for X_test.
Display predicted values along with actual values.
3.Calculate model accuracy using accuracy_score. Display the result in percentage format.
4. Generate confusion matrix using sklearn.
Display it using Confusion Matrix Display.
Explain clearly:
True Positive
True Negative
False Positive
False Negative
5. Calculate:
Training accuracy
Testing accuracy
Compare both and comment whether the model is overfitting or underfitting.
6. Train three Decision Tree models with:
max_depth = 1
max_depth = 3
max_depth = None
Compare their testing accuracies and write your observations.
2/3
7. Use the trained model to predict result for a student with:
StudyHours = 6
Attendance 85
PreviousScore = 66
AssignmentsCompleted = 7
SleepHours = 7

Will the student Pass or Fail?
8. Write a single structured Python program that performs:
1. Dataset loading
2. Data analysis
3. Visualization
4. Train-test split
5. Model training
6. Prediction
7. Accuracy calculation
8. Confusion matrix generation
9. Final conclusion
Your code should include proper comments explaining each step."""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import pandas as pd
import matplotlib.pyplot as plt


Border="-"*40
print(Border)
print(" Dataset loading")
print(Border)

df=pd.read_csv("student_performance_ml.csv")
print(df)

#Data analysis
print(Border)
print("Data analysis")
print(Border)

#head data
print(df.head())
#tail data
print(df.tail())

#Total number of rows and columns
print("Total number of rows and columns")
print(df.info())


#Visualization
print(Border)
print("Visualization")
print(Border)

#List of column names
print("#List of column names")
print(df.columns.tolist())

# Input features
X = df[["StudyHours", "Attendance", "PreviousScore",
    "AssignmentsCompleted", "SleepHours"]]

# Target variable
Y = df["FinalResult"]
print(Border)



#1.Import Decision Tree Classifier from sklearn.
# Create a model object and train it using fit()
print(Border)
print("Train-test split")
print(Border)


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
#Creat a module
model=DecisionTreeClassifier()

model.fit(X_train,Y_train)
print("Decision Tree model trained successfully")
print(Border)


#2. Use the trained model to predict results for X_test.
#Display predicted values along with actual values.
print(Border)
print("Model training Prediction")
print(Border)

#Display prediction result of X_test
Y_pred=model.predict(X_test)

#Display the predict and actual value
print("Prediction value is :",Y_pred)
print("Actual value is :",Y_test.values)
print(Border)


#3.Calculate model accuracy using accuracy_score. Display the result in percentage format.
print(Border)
print("Accuracy calculation")
print(Border)

#Calculate the accuracy
Accuracy=accuracy_score(Y_test,Y_pred)

#Display the Accuracy in parcentages
print("Accuracy:",Accuracy * 100,"%")
print(Border)

#Generate confusion matrix using sklearn.
#Display it using Confusion Matrix Display.
#Explain clearly:
#True Positive
#True Negative
#False Positive
#False Negative
print(Border)
print("confusion matrix")
print(Border)

#generates the confusion matrix
cm=confusion_matrix(Y_test,Y_pred)
print("confusion_matrix")
print(cm)
 
#Display the confusion matrix
disp=ConfusionMatrixDisplay(confusion_matrix=cm,
     display_labels=["Fail","Pass"])
disp.plot()
plt.show()

#Calculate:
#Training accuracy
#Testing accuracy
#Compare both and comment whether the model is overfitting or underfitting.
print(Border)
print("Training accuracy and Testing accuracy")
print(Border)

#predicts traning data
Y_train_pred=model.predict(X_train)
Y_test_pred=model.predict(X_test)

# Calculate training accuracy
train_accuracy=accuracy_score(Y_train_pred,Y_train_pred)

# Calculate testing  accuracy
test_accuracy=accuracy_score(Y_test_pred,Y_test_pred)

# Display in percentage
print("training accuracy:",train_accuracy * 100,"%")
print("testing  accuracy:",test_accuracy *100,"%")

print(Border)

#6.Train three Decision Tree models with:
#max_depth = 1
#max_depth = 3
#max_depth = None
print(Border)
print("Decision Tree Models with Different max_depth")
print(Border)
# Model 1: max_depth = 1
model1 = DecisionTreeClassifier(max_depth=1)
model1.fit(X_train, Y_train)

Y_pred1 = model1.predict(X_test)
accuracy1 = accuracy_score(Y_test, Y_pred1)


# Model 2: max_depth = 3
model2 = DecisionTreeClassifier(max_depth=3)
model2.fit(X_train, Y_train)

Y_pred2 = model2.predict(X_test)
accuracy2 = accuracy_score(Y_test, Y_pred2)


# Model 3: max_depth = None
model3 = DecisionTreeClassifier(max_depth=None)
model3.fit(X_train, Y_train)

Y_pred3 = model3.predict(X_test)
accuracy3 = accuracy_score(Y_test, Y_pred3)


# Display testing accuracies
print(Border)
print("Testing Accuracies")
print(Border)

print("Model 1 (max_depth=1):", accuracy1 * 100, "%")
print("Model 2 (max_depth=3):", accuracy2 * 100, "%")
print("Model 3 (max_depth=None):", accuracy3 * 100, "%")

print(Border)

#7. Use the trained model to predict result for a student with:
#StudyHours = 6
#Attendance 85
#PreviousScore = 66
#AssignmentsCompleted = 7
#SleepHours = 7
print(Border)
print("Use the trained model to predict result for a student")
print(Border)

#Student data
student=[[6,85,66,7,7]]

prediction=model2.predict(student)

print("Student Data")
print("StudyHours :",6)
print("Attendance :",85)
print("PreviousScore :",66)
print("AssignmentsCompleted :",7)
print("SleepHours :",7)

print("prediction result:",prediction[0])
if prediction[0]==1:
    print("Student is Pass")
else:
    print("Student is fail")

