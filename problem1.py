
print("Problem 1: Calculator")

class Calculator:
    def __init__(self, a, b, op):   
        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid Operation")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

Calculator(a, b, op)   
