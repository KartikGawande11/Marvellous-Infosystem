'''Machine Learning Assignment

Q1: Normalize the 'Math' scores using Min-Max scaling.

Q2: Create a gender column and perform one-hot encoding.

Q3: Group students by gender and calculate average marks.

Q4: Plot a pie chart of subject marks for 'Sagar'.

Q5: Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'.

Q6: Count how many students passed.

Q7: Export the final DataFrame to a CSV file.

Q8: Plot a histogram of math marks.

Q9: Rename 'Math' column to 'Mathematics'.

Q10: Plot a boxplot for English marks to check distribution and outliers'''

######################################################################################
import pandas as pd
import matplotlib.pyplot as plt

Border="-"*40
print(Border)
print(" Normalize the 'Math' scores using Min-Max scaling.")
print(Border)
data = {

'Name': ['Amit', 'Sagar', 'Pooja'],

'Math': [85, 90, 78],

'Science': [92, 88, 80],

'English': [75, 85, 82]

}
df=pd.DataFrame(data)
print(df)
print(Border)

result=df['Math'].max()
print("Max valeu is :",result)
print(Border)

result1=df['Math'].min()
print("Min Value is:",result1)
print(Border)

#########################################################
#Q2: Create a gender column and perform one-hot encoding.
#########################################################

print(Border)
print("Create a gender column and perform one-hot encoding.")
print(Border)

# Create Gender column
df["Gender"] = ["Male", "Male", "Female"]

print(df)
print(Border)
# Save original DataFrame for Q3
df_gender = df.copy()

# One-Hot Encoding
print(Border)
print(" One-Hot Encoding")
print(Border)
df = pd.get_dummies(df, columns=["Gender"])
print(df)
print(Border)

##########################################################
#Q3: Group students by gender and calculate average marks.
###########################################################
print(Border)
print("Group students by gender and calculate average marks.")
print(Border)

res = df_gender.groupby("Gender")[["Math", "Science", "English"]].mean()
print(res)
print(Border)
####################################################################
#Q4: Plot a pie chart of subject marks for 'Sagar'.
####################################################################
print(Border)
print(": Plot a pie chart of subject marks for 'Sagar'.")
sagar = df[df["Name"] == "Sagar"]

marks = sagar[["Math", "Science", "English"]].values[0]

plt.pie(
    marks,
    labels=["Math", "Science", "English"],
    autopct="%1.1f%%"
)

plt.title("Sagar's Subject Marks")
plt.show()

print(Border)

##########################################################
# Q5: Add a new column 'Status'
# Students with total >= 250 are Pass, else Fail.
##########################################################

print(Border)
print("Add a new column 'Status'")
print(Border)

# Calculate total marks
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Create Status column
df["Status"] = df["Total"].apply(
    lambda x: "Pass" if x >= 250 else "Fail"
)

print(df)

print(Border)

#Q6: Count how many students passed.
res1=(df["Status"]=="pass").sum()
print(res1)