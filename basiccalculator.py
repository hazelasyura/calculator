def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Choose operation:")
    print("+. Add")
    print("-. Subtract")
    print("*. Multiply")
    print("/. Divide")

    choice = input("Choose an operation (+/-/*/(/)): ")

    if choice in ['+', '-', '*', '/']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(f"The answer is: {add(num1, num2)}")
        elif choice == '-':
            print(f"The answer is: {subtract(num1, num2)}")
        elif choice == '*':
            print(f"The answer is: {multiply(num1, num2)}")
        elif choice == '/':
            print(f"The answer is: {divide(num1, num2)}")
    else:
        print("Wrong input")

if __name__ == "__main__":
    calculator()
