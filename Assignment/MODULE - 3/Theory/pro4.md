#### Converting user input into different data types (e.g., int, float, etc.).

##### 1.Converting Input to Integer (int)
If you need to accept an integer value from the user, you can convert the string input into an integer using the int() function.

```python
age = int(input("Enter your age: "))  
print(f"Age is :{age}")
```
##### 2. Converting Input to Float (float)
- If you need to accept a floating-point number, you can convert the string input into a float using the float() function.

```python

height = float(input("Enter height :"))
print(f"Height is:{height}")
```

#### 3. Converting Input to Boolean (bool)
- To convert user input into a boolean (True or False), you can compare the input string to specific values (like "yes" or "no") or use a direct conversion, but Python's bool() function can also be used for basic truthy/falsy conversions.

```python
wants_to_continue = input("Do you want to continue (yes/no)? ").lower() == "yes"

if wants_to_continue:
    print("You chose to continue!")
else:
    print("You chose not to continue.")
```