#Write a Python program to handle exceptions in a calculator. 


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def add(a,b):
    if b == 0:
         raise ValueError("Cannot divide by zero!")
    return a + b

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = input("Enter choice (1/2/3/4): ")

            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please select a valid operation.")
                continue

            num1 = get_float_input("Enter first number: ")
            num2 = get_float_input("Enter second number: ")

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {mul(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {div(num1, num2)}")

        except ValueError as e:
            print(f"Error: {e}")
        finally:
            again = input("Do you want to perform another calculation? (yes/no): ").lower()
            if again != 'yes':
                print("Exiting the calculator.")
                break

if __name__ == "__main__":
    calculator()
