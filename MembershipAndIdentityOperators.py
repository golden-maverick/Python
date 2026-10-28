# Practical 8_A: Membership and Identity Operators

# Membership operators
list1 = list(map(int, input("Enter elements of list1: ").split()))

num1 = int(input("Enter number to check using 'in': "))

if num1 in list1:
    print(num1, "is present in list1")
else:
    print(num1, "is not present in list1")

num2 = int(input("Enter number to check using 'not in': "))

if num2 not in list1:
    print(num2, "is not present in list1")
else:
    print(num2, "is present in list1")
    
# Identity operators
a = list(map(int, input("Enter elements of list a: ").split()))
b = a
c = list(map(int, input("Enter elements of list c: ").split()))

if a is b:
    print("a and b are identical")
else:
    print("a and b are not identical")

if a is not c:
    print("a and c are not identical")
else:
    print("a and c are identical")