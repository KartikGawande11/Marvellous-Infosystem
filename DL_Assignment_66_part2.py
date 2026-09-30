"""2: Write a Python program to demonstrate different activation functions.

Functions to implement:

1. Sigmoid

2. ReLU

3. Tanh

Tasks:

1. Accept input values from 10 to 10.

2. Plot all activation functions using Matplotlib.

3. Explain the use of each activation function."""


# ---------------------------------------------------------
#1. Accept input values from - 10 to 10.
# ---------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

X=np.linspace(-10,10.1000)


# ---------------------------------------------------------
# Step 2: Functions to implement:
#Relu,sigmoid,Tanh Activation function
# ---------------------------------------------------------

#1. ReLU
def relu(X):
    return np.maximum(0,X)

#2.Sigmoid
def Sigmoid(X):
    return 1/(1+np.exp(-X))

#3. Tanh
def Tanh(X):
    return np.tanh(X)

# ---------------------------------------------------------
# Step 3: Calculate activation function outputs
# ---------------------------------------------------------

relu_output=relu(X)
sigmoid_output=Sigmoid(X)
tanh_output=Tanh(X)

# ---------------------------------------------------------
# step 4:Plot all activation functions using Matplotlib.
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))

plt.plot(X, sigmoid_output, label="Sigmoid")
plt.plot(X, relu_output, label="ReLU")
plt.plot(X, tanh_output, label="Tanh")

plt.title("Activation Functions")
plt.xlabel("Input")
plt.ylabel("Output")

plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

plt.grid(True)
plt.legend()

plt.show()



