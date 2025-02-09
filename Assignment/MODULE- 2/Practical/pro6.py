"""Write a Python program to insert elements into an empty list using a for loop and
append().
"""
list =[]
x = int(input("How many element to inserted :"))

for i in range(x):
    element = input(f"Enter element {i + 1}:")
    list.append(element)
print(list)