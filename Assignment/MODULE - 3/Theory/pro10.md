#### Introduction to exceptions and how to handle them using try, except, and finally.

- Exceptions in Python are errors that occur during the execution of a program. When an exception occurs, Python stops executing the current block of code and looks for a way to handle the error. If no error-handling mechanism is found, the program terminates with an error message.

<b>1.try block:</b>
- Contains the code that might raise an exception.

<b>except block:</b>
- Executes only if an exception occurs in the try block. You can specify different types of exceptions to handle specific errors.

<b>finally block (Optional):</b>
- Executes no matter what, whether an exception occurs or not. It is often used for cleanup actions like closing files or releasing resources.

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
      print("Execution completed.")
```