"""Write a Python program to create a file and write a string into it.
"""
import os
os.chdir("Practical") 

file = open("text.txt",'a')

name = input("Enter name :")

file.write(f"Name is :{name}")