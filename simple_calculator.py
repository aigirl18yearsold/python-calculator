
def calculator():
    print("Simple Calculator")
    print("Choose operation: +, -, *, /")
    
    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))
    
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid operator"
    
    print("Result:", result)

calculator()
