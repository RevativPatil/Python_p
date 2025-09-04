x=int(input("Enter first number"))
y=int(input("Enter second number"))
try:
    z=x/y
    print("Division is",z)
except ZeroDivisionError:
    print("Don't devide by zero")
    z=0
