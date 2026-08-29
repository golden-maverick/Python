print("Enter the value of x1:")
x1= int(input())
print("Enter the value of x2:")
x2= int(input())
print("Enter the value of w1:")
w1= int(input())
print("Enter the value of w2:")
w2= int(input())
# Calculated weighted sum
weighted_sum = (x1 * w1) + (x2 * w2)
print("The weighted sum is:", weighted_sum)
yin= weighted_sum
print("net input to the neural nectwork is:", yin)
if yin <= 0:
    yout=0
else:
    yout=1
print("The output of the neural netweok is:", yout)
