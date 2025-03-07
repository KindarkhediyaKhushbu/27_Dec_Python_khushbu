"""Write a Python program to open a file in write mode, write some text, and then close it."""
import os

os.chdir("Lab")
file = open("test.txt" ,'w')

file.write("This is python")

file.close()