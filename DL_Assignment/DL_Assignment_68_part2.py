"""Write a Python program to demonstrate ReLU and Max Pooling.

Tasks:

,

1. Create a feature map with positive and negative values.

2. Apply ReLU.

3. Apply 2x2 max pooling.

4. Display output after each step.

5. Explain why pooling reduces size.

Input Feature Map

feature_map = [

[3, 3, 3],

[0,0,0],

[-3, -3, -3]

]

ReLU Rule

If value < 0, convert it to 0 If value >= 0, keep it same

Expected Output

relu_output = [

[3, 3, 3],

[0,0,0],

[0,0,0]

]
"""
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D


#------------------------------------------------------------------------------
# step1:-1. Create a feature map with positive and negative values.
#------------------------------------------------------------------------------

feature_map = [

[3, 3, 3],
[0,0,0],
[-3, -3, -3]

]

#------------------------------------------------------------------------------
#step2:-2. Apply ReLU.
#------------------------------------------------------------------------------

relu=np.maximum(0,feature_map)
print("\nReLU Feature Map:")
print(relu)


#------------------------------------------------------------------------------
#step 3:3. Apply 2x2 max pooling.
#------------------------------------------------------------------------------

pooling=np.zeros((2,2))
for i in range(2):
    for j in range(2):
        region=relu[i:i+2,j:j+2]
        pooling[i,j]=np.max(relu)
        
print("\n2x2 Max Pooling:")
print(pooling)


#------------------------------------------------------------------------------
# Step 4: Display output after each step
#------------------------------------------------------------------------------

print("\n================ FINAL OUTPUT ================")

print("\n1. Feature Map:")
print(feature_map)

print("\n2. ReLU Output:")
print(relu)

print("\n3. Max Pooling Output:")
print(pooling)