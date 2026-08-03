operator=input("Enter an operator (+ - * /):")
num1=float(input("Enterypur first number:"))
num2=float(input("Enter your second number:"))

if operator=="+":
    result=num1+num2
    print("The result of addition is:",result)
elif operator=="-":
    result=num1-num2
    print("The result of subtraction is:",result)
elif operator=="*":
    result=num1*num2
    print("The result of multiplication is:",result)
elif operator=="/":
    if num2!=0:
        result=num1/num2
        print("The result of division is:",result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")