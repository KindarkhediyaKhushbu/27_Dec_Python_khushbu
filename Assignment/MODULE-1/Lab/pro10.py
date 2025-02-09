#Practical Example 7: Write a Python program to calculate grades based on percentage using if-else ladder.

percentage = int(input("Enter your Percentage :"))

if percentage >= 90:
    print("Grades is A+")
elif percentage >= 80:
    print("Grades is A")
elif percentage >= 70:
    print("Grades is B")
elif percentage >= 60:
    print("Grades is C")
elif percentage >= 50:
    print("Grades is D")
elif percentage >= 45:
    print("Grades is avarage")
else :
    print("You are fail!")
    