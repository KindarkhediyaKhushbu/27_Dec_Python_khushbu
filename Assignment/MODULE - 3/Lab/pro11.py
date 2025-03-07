'''Write a Python program to search for a word in a string using re.search().'''

import re

x = "This is Python!"

result = re.search("Python", x)

if result:
    print("Match Done...")
else:
    print("Error!")