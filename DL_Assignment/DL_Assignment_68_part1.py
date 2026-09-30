"""Deep Learning Assignment

1: Write a Python program to manually perform convolution.

Input:

A 5x5 matrix representing grayscale image.

Kernel:

A 3x3 edge detection filter.

Tasks:

1. Move kernel over image.

2. Perform multiplication and addition.

3. Generate feature map.

4. Print each region calculation.

Input Image Matrix

image = [

[0,0,0,0,0],

[0,0,0,0,0],

[1, 1, 1, 1, 1],

[0,0,0,0,0],

[0,0,0,0,0]

]

Kernel Matrix

kernel = [

[-1, -1, -1],
[0, 0, 0],
[1, 1, 1]

]

First Region Calculation

Region:

000
000
111

Kernel:

-1,-1,-1
0,0,0
1,1,1

"""

#------------------------------------------------------------------------------
#Step 1:A 5x5 matrix representing grayscale image.
#------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D

image = [

[0,0,0,0,0],

[0,0,0,0,0],

[1, 1, 1, 1, 1],

[0,0,0,0,0],

[0,0,0,0,0]

]
print("5x5 matrix representing grayscale image.")
print(image)


#----------------------------------------------------------------------------
#Step 2 3x3 edge detection filter.
#1. Move kernel over image.

#----------------------------------------------------------------------------

kernel = [

[-1, -1, -1],

[0, 0, 0],

[1, 1, 1]

]
print("3x3 edge detection filter.")
print(kernel)

#------------------------------------------------------------------------------
#Step 3:3. Generate feature map.
#------------------------------------------------------------------------------
image=np.array(image)
kernel=np.array(kernel)

#get image and kernal size

image_height,image_width=image.shape
kernel_height,kernel_width=kernel.shape

#calculate feature map size:
feature_map_hight=image_height-kernel_height+1
feature_map_width=image_width-kernel_width+1


# Create empty feature map
feature_map=np.zeros(
    (feature_map_hight,feature_map_width)
)

print(feature_map)

#------------------------------------------------------------------------------
# Step 4: Move kernel over image
#------------------------------------------------------------------------------

for i in range(feature_map_hight):
    for j in range(feature_map_width):
          # Get current 3x3 region
        region = image[
            i:i + kernel_height,
            j:j + kernel_width
        ]
        
        # Multiplication
    multiplication = region * kernel

        # Addition
    result = np.sum(multiplication)

        # Store result in feature map
    feature_map[i, j] = result

    print("\nRegion:")
    print(region)

    print("\nKernel:")
    print(kernel)

    print("\nMultiplication:")
    print(multiplication)

    print("\nSum:")
    print(result)
#------------------------------------------------------------------------------
# Step 5: Print Feature Map
#------------------------------------------------------------------------------

print("\nFinal Feature Map:")
print(feature_map)