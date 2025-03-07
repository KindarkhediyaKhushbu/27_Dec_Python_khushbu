# Write a Python program to write multiple strings into a file.

line = [
    "My name is khushbu kindarkhediya\n",
    "I am form junagadh",
]

import os
os.chdir("Lab")
with open("example.txt",'w') as files:
    files.writelines(line)
    
print('example.txt')
