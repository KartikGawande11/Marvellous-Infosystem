"""Write a Python program to calculate loss manually.

Tasks:

1. Implement Mean Squared Error.

2. Implement Binary Cross Entropy.

3. Take actual and predicted values.

4. Display the calculated loss.

5. Explain which loss function is used for regression and classification.
"""

import math

#----------------------------------------------------------------
# step1: Implement Mean Squared Error.
#----------------------------------------------------------------

actual=[1,0,1,1]
predictes=[0.9,0.2,0.8,0.7]

def Mean_Squared_Error(actual,predictes):
    total=0
    for a,p in zip(actual,predictes):
        total+=(a-p)**2
    return total / len(actual)

mse=Mean_Squared_Error(actual,predictes)

#-----------------------------------------------------------------
#step:2 2. Implement Binary Cross Entropy.
#-----------------------------------------------------------------


def Binary_Cross_Entropy(actual,predictes):
    total=0
    for a,p in zip(actual,predictes):
        total+=-(a * math.log(p) + (1 - a) * math.log(1 - p))
    return total / len(actual)
bce = Binary_Cross_Entropy(actual, predictes)


# ---------------------------------------------------------
# 3. Display calculated losses
# ---------------------------------------------------------

print("Actual values    :", actual)
print("Predicted values :", predictes)

print("Mean Squared Error =", mse)
print("Binary Cross Entropy =", bce)
        
