#### Difference between local and global variables.

##### Local variables:
- Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function. Let’s see how to create a local variable.

```python
def f():
    s = "I love Geeksforgeeks"
    print(s)
f()
```

##### Global variables:
- These are those which are defined outside any function and which are accessible throughout the program, i.e., inside and outside of every function. Let’s see how to create a Python global variable.

```python
def f():
    print("Inside Function", s)
s = "I love India"
f()
print(s)
```