#Practical Example 8: Write a Python program to check if a person is eligible to donate blood using a nested if.

per = int(input("Enter your age :"))

if per >= 18:
    if per < 50:
        print("person is eligible to donate blood") 
    else:
        print("person is over age ")
else:
    print(" person is under age ")
    