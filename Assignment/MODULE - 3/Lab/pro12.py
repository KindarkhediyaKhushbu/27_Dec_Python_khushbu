'''Write a Python program to match a word in a string using re.match().'''

import re

x = "This is Python!"

result = re.match("This", x)

if result:
    print("Match Done...")
else:
    print("Error!")
    