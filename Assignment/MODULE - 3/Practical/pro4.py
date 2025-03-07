"""Write a Python program to create a file and print the string into the
file. """
import os
os.chdir("Practical") 

file = open("First.txt","a")

x = input("Enter string")

file.write(x)
