'''Practical Example 4: Print this pattern using nested for loop:
markdown
Copy code
*
**
***
****
*****'''

for i in range(1,6): 
    for k in range(i): 
        print("*",end=" ")
    print(" ") 