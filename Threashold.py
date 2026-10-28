# weights
w1 = 1
w2 = 1

# inputs
x1 = 1
x2 = 1

# Threshold
threshold = 2

# Calculate weighted sum
net = (x1 * w1) + (x2 * w2)

# Apply threshold function
if net >= threshold:
    output = 1
else:
    output = 0

# Display result
print("Weighted Sum =", net)
print("Output =", output)