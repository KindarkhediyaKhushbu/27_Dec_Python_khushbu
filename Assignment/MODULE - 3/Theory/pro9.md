#### Writing to a file using write() and writelines().

1. write()
- Writes a single string to a file.
- Use this method when you want to write a single piece of data (typically a string) to the file. If the file does not exist, Python will create it. If it already exists, it will overwrite the content unless you open the file in append mode.
Example:

```python
with open('example.txt', 'w') as file: 
    file.write("Hello\n")
    file.write("This is another line.")
```

2. writelines()
- Writes a list (or any iterable) of strings to a file. Each string in the list will be written consecutively without adding a newline unless explicitly included in the string.
- This is useful when you have multiple lines or a collection of strings to write to a file.
Example:

```python
lines = [
    "First line of text.\n",
    "Second line of text.\n",
    "Third line of text."
]

with open('example.txt', 'w') as file:  
    file.writelines(lines)
```