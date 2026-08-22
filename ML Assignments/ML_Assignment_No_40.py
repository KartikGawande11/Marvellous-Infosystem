"""Machine Learning
Dataset Description - Student Performance ML Dataset
The dataset student_performance_ml.csv contains academic and behavioral
information of students. The objective of this dataset is to predict whether a
student will Pass (1) or Fail (0) based on various input features.
Each row in the dataset represents one student, and each column represents a
measurable factor that may influence academic performance.
Features Description
StudyHours - Number of hours a student studies per day.
Attendance - Percentage of class attendance.
PreviousScore - Marks obtained in the previous examination.
AssignmentsCompleted - Number of assignments completed by the student.
SleepHours - Average number of hours the student sleeps per day.
Final Result - Target variable (Output):

1 → Pass
0→ Fail
Objective of the Dataset
The goal is to:
Analyze how different factors affect student performance.
Build a Machine Learning model to predict whether a student will pass or fail.
Understand concepts such as training, testing, accuracy, confusion matrix, overfitting,
and model evaluation

1. After training the Decision Tree model, use:
model.feature_importances_
Display importance score of each feature.
Which feature contributes the most in predicting FinalResult?
Which feature contributes the least?

2. Remove the column SleepHours from the dataset.
Train the model again.
Compare new accuracy with previous accuracy.
Does removing this feature affect performance?

3. Train the model using only:
Study Hours
Attendance
Compare the accuracy with the full-feature model.
Is the model still performing well?

4. Create a new DataFrame with details of 5 new students.
Use the trained model to predict their results.
Display predictions clearly.

5. Without using accuracy_score, manually calculate accuracy:
Verify whether it matches sklearn accuracy.

6. Identify students where:
y_test != y_pred
Display those rows.
How many students were misclassified?
What common pattern do you observe?

7. Train model using:
random state = (0
random_state = 10
random_state = 42
Compare testing accuracy.
Does the result change?

8. Decision Tree Visualization
Use:
from sklearn.tree import plot tree
Visualize the trained decision tree.
Which feature appears at the root node?
Why do you think that feature was selected first?

9. Create a new column:
PerformanceIndex = (StudyHours * 2) + Attendance
Train the model including this new feature.
Does accuracy improve?

10. Train model with:
max_depth = None
Calculate:
Training accuracy
Testing accuracy
If training accuracy is 100% but testing accuracy is lower, explain why this happens."""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd


Border="-"*40
print(Border)

df=pd.read_csv("student_performance_ml.csv")
print(df)
# Independent features
X = df.drop("FinalResult", axis=1)

# Dependent feature
y = df["FinalResult"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

#1. After training the Decision Tree model, use:
#model.feature_importances_
#Display importance score of each feature.
#Which feature contributes the most in predicting FinalResult?
#Which feature contributes the least?
print(Border)
print("model.feature_importances_")
print(Border)

importance=model.feature_importances_

#Display importance score of each featurs
for feature,score in zip(X.columns,importance):
    print(feature,":",score)
    
#finde the most importanat feature
most_important=X.columns[importance.argmax()]

#finde the least importanat feature
most_least_importanat=X.columns[importance.argmin()]

print(Border)
print("most_importan is :",most_important)
print("most_least_importanat is :",most_least_importanat)
print(Border)


#2. Remove the column SleepHours from the dataset.
#Train the model again.
#Compare new accuracy with previous accuracy.
#Does removing this feature affect performance?
