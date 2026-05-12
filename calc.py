def Addition(a, b):
    return a + b

def Subtraction(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Divison(a,b):
    if b == 0:
        return "Division by zero is not possible"
    return a/b


num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

op=input("Enter operation(+,-,*,/) you have to perform:")

if op=='+':
    print("Ans:",Addition(num1,num2))
elif op=='-':
    print("Ans:",Subtraction(num1,num2))
elif op=='*':
    print("Ans:",Multiplication(num1,num2))
elif op=='/':
    print("Ans:",Divison(num1,num2))
else:
    print("Operation is invalid....")
