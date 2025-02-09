#Write a Python program to merge two lists into one dictionary using a loop.

key = ["name",'age','city']
val = ['khushbu','21','junagadh']

merge_dict = {}

for i in range(len(key)):
    merge_dict[key[i]] = val[i]

print(merge_dict)    