"""
3: Write a Python program to show flattening.

Tasks:

1. Take a 2D matrix.

2.Convert it into a 1D vector. 2.

3.Pass it to a fully connected layer. 3.

4. Calculate final output manually.

5. Explain the role of flatten layer in CNN.

Input Matrix

matrix = [

[6, 4],

[8, 6]

]

Expected Flatten Output

flatten_output = [6, 4, 8, 6]
"""
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D


#------------------------------------------------------------------------
# Step 1:-1. Take a 2D matrix.
#------------------------------------------------------------------------

matrix =np.array([

[6, 4],

[8, 6]

])

#----------------------------------------------------------------------
#step 2:-2 Convert it into a 1D vector.
#----------------------------------------------------------------------

flatten_output = matrix.flatten()

print("\nFlatten Output:")
print(flatten_output)

#------------------------------------------------------------------------
# Step 3: Pass it to a Fully Connected Layer
#------------------------------------------------------------------------

weights = np.array([1, 2, 1, 2])
bias=1

print("\nWeights:")
print(weights)

print("\nBias:")
print(bias)

#------------------------------------------------------------------------
# Step 4: Calculate final output manually
#------------------------------------------------------------------------
weighted_sum =np.sum(flatten_output*weights)
final_output = weighted_sum + bias

print("\nWeighted Sum:")
print(weighted_sum)

print("\nFinal Output:")
print(final_output)