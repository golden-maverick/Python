# Hebb's Rule in ANN
# Initialize values
x = 1
y = 1
w = 0.2
eta = 0.5
# Calculate weight change
delta_w = eta * x * y
# Update weight
w = w + delta_w
# Display results
print("Weight change:", delta_w)
print("Updated weight:", w)