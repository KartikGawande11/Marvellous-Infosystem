"""Deep Learning Assignment

1: Write a Python program to simulate a single artificial neuron.

Input:

x1 2 x2 3 w1 0.4 w2 0.6

bias 0.5

Tasks:

1. Calculate weighted sum.

2. Apply sigmoid activation function.

3. Display final output.

4. Explain whether output is close to 0 or 1."""
 
###################################################################
# Step 1 :1. Calculate weighted sum.
###################################################################
import math
X1=2
X2=3
W1=0.4
W2=0.6
bias=0.5

#x1*w1+x2*w2+bias

result=(X1*W1)+(X2*W2)+bias
print(" Calculate weighted sum.",result)


###################################################################
# Step 2 :. Apply sigmoid activation function.
###################################################################


output=1/(1+math.exp(-result))
print("sigmoid activation function.",output)

###################################################################
# 3. Display final output.
###################################################################

print("Display final output.",output)

###################################################################
#4. Explain whether output is close to 0 or 1
###################################################################

if output >=0.5:
    print("The output is close to 1.")
    
else:
    print("The output is close to 1.")
    
