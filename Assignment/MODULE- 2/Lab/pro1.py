''' Write a Python program to create a list with elements of multiple data types (integers,
strings, floats, etc.).'''

list = [21, "khushbu", 2.10, [1, 2, 3]]

for item in list:
    print(f"Value: {item}, Type: {type(item)}")