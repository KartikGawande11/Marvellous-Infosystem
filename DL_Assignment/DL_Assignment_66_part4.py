"""4: Write a Python program to show how weights are updated in ANN.

Tasks:

1. Take input, weight, bias, target output, and learning rate.

2. Calculate prediction.

3. Calculate error.

4. Update weight using gradient descent logic.

5. Display old weight and updated weight.

"""
#----------------------------------------------------------
# Step 2:-Take input, weight, bias, target output, and learning rate.
#----------------------------------------------------------
x=9
weight=0.15
bias=0.30
target_output=8
learning_rate=0.11


#----------------------------------------------------------
# Step 2:-2. Calculate prediction.
#----------------------------------------------------------

prediction=(x*weight)+bias
print("prediction is =",prediction)

#----------------------------------------------------------
# step 3. Calculate error.
#----------------------------------------------------------

error=target_output-prediction
print("error is =",error)

#----------------------------------------------------------
#step 4. Update weight using gradient descent logic.
#----------------------------------------------------------
old_weight=weight
weight=weight-learning_rate*error*x
print("Old Weight =", old_weight)
print("Updated Weight =", weight)
