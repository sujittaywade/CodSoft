# This Function is to perform addition
def add(x, y):
    return x + y

# This Function  is to perform subtraction
def subtract(x, y):
    return x - y

# This Function is to perform multiplication
def multiply(x, y):
    return x * y

# This Function is to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

# Prompt the user to input two numbers and an operation choice
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number:"))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4):")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        else:
            result = divide(num1, num2)
            operation = '/'

        print(f"{num1} {operation} {num2} = {result}")
    else:
        print("Invalid input. Please choose a valid operation (1/2/3/4).")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
