import math

def calculator():
    print("Simple Advanced Calculator")
    print("Operations: +, -, *, /, sqrt, pow, sin, cos, tan, log")

    while True:
        op = input("\nEnter operation (or 'exit' to quit): ")

        if op == 'exit':
            break
        elif op in ['+', '-', '*', '/']:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if op == '+':
                print("Result:", a + b)
            elif op == '-':
                print("Result:", a - b)
            elif op == '*':
                print("Result:", a * b)
            elif op == '/':
                if b == 0:
                    print("Error: Division by zero")
                else:
                    print("Result:", a / b)
        elif op == 'sqrt':
            x = float(input("Enter number: "))
            print("Result:", math.sqrt(x))
        elif op == 'pow':
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print("Result:", math.pow(base, exp))
        elif op in ['sin', 'cos', 'tan']:
            angle = float(input("Enter angle in degrees: "))
            radians = math.radians(angle)
            if op == 'sin':
                print("Result:", math.sin(radians))
            elif op == 'cos':
                print("Result:", math.cos(radians))
            elif op == 'tan':
                print("Result:", math.tan(radians))
        elif op == 'log':
            x = float(input("Enter number: "))
            print("Result:", math.log(x))
        else:
            print("Invalid operation")

calculator()