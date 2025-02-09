# Write a Python program to convert two lists into one dictionary using a for loop.

key = ["name",'age','city']
val = ['khushbu','21','junagadh']

dict = {}

for i in range(len(key)):
    dict[key[i]] = val[i]

print(dict)    