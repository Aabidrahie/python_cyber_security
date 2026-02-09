a = int(input("Enter the first number:     "))

char = input("Enter the operation (+, -, *, /):    ")
b = int(input("Enter the second number:     "))
if char == '+':
    print("The sum is: ", a + b)
elif char == '-':
    print("The difference is: ", a - b)
elif char == '*':
    print("The product is: ", a * b)
elif char == '/':
    if b != 0:
        print("The quotient is: ", a / b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation entered.")