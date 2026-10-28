# Practical 8_B: Identity Operators (is, is not)
# Using 'is' operator
x = eval (input ("Enter a value for x: "))

if type (x) is int:
    print ("True")
else:
    print ("False")

# Using 'is not' operator
y = eval (input("Enter a value for y: "))
if type (y) is not int:
    print ("True")
else:
    print ("False")