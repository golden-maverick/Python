import math

# input
x1=1
x2=2

# weights
w1=0.5
w2=0.5

# bias
b=1

# Calculated weighted sum
net = (x1 * w1) + (x2 * w2)+b
print("Net input:", net)

# Binary Sigmoid

binary_output = 1/(1+math.exp(-net))

# Bipolar Sigmoid

bipolar_output = (2/(1+math.exp(-net)))-1

print("Binary Sigmoid Output:", binary_output)

print("Bipolar Sigmoid Output:", bipolar_output)