#### Understanding multiple exceptions and custom exceptions.

<b>1. Handling Multiple Exceptions</b>
- You can catch multiple exceptions by specifying more than one exception type in a try-except block. This allows you to handle different types of errors in a specific manner.
- Example

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

<b>2. Custom Exceptions</b>
- You can create your own custom exceptions by subclassing the built-in Exception class. This allows you to create specific error messages or error types for your application.

- Example

```python
class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers not allowed!")

try:
    num = int(input("Enter a number: "))
    check_number(num)
except NegativeNumberError as e:
    print(f"Error: {e}")

```

