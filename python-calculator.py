def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero"
    return x % y

def calculator():
    print("Simple Calculator")
    print("Operations: Add, Subtract, Multiply, Divide, Modulus")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation: ").lower()

            if operation == "add":
                result = add(num1, num2)
            elif operation == "subtract":
                result = subtract(num1, num2)
            elif operation == "multiply":
                result = multiply(num1, num2)
            elif operation == "divide":
                result = divide(num1, num2)
            elif operation == "modulus":
                result = modulus(num1, num2)
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"Result: {result}")
            
            again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if again != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
