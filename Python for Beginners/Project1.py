#  Project 1: Simple Calculator (Using Functions & Conditionals)
def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def multiply(a, b): 
    return a * b
def divide(a, b): 
    return a / b if b != 0 else "Cannot divide by zero"


while True:
    print("\nOptions: add, subtract, multiply, divide, exit")
    choice = input("Choose operation: ")

    if choice == "exit":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "add":
        print("Result:", add(num1, num2))
    elif choice == "subtract":
        print("Result:", subtract(num1, num2))
    elif choice == "multiply":
        print("Result:", multiply(num1, num2))
    elif choice == "divide":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice.")
