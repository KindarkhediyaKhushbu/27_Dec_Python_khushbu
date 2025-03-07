#### Method overloading: defining multiple methods with the same name but different parameters.

1. Using Default Arguments
You can define a single method that handles different numbers of arguments by providing default values for some parameters.

2. Using Variable-Length Arguments
The *args and **kwargs syntax allows you to pass a variable number of arguments to a method.


```python
class Calculator:
        def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()


print("Sum of 2 numbers:", calc.add(10, 20))        
print("Sum of 3 numbers:", calc.add(10, 20, 30))     
print("Sum with one number:", calc.add(10))           
```