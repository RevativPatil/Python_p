a=eval(input("Enter first number\n"))
b=eval(input("Enter second number\n"))
o=input("Enter Operator\n '+' , '-' , '*' , '/' , '%' ")

if(o=='+'):
    print(f"Addition of {a} and {b} is {a+b}")
elif(o=='-'):
    print(f"Subtraction of {a} and {b} is {a-b}")
elif(o=='*'):
    print(f"Multiplication of {a} and {b} is {a*b}")
elif(o=='/'):
    print(f"Division of {a} and {b} is {a-b}")
elif(o=='%'):
    print(f"Remainder of {a} and {b} is {a-b}")
else:
    print("invalid operator")