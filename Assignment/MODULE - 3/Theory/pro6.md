#### Using the open() function to create and access files.

###### 1: Creating and Writing to a File
If you want to create a file and write content to it, you can use the 'w' mode.

```python
file = open('example.txt', 'w')  
file.write("Hello,")  
file.close() 
```