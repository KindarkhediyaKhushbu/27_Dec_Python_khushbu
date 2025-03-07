#### Reading from a file using read(), readline(), readlines().

1. read()
- Reads the entire file content as a single string.
- Use this when you want to load the whole file at once.
Example:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```
2. readline()
- Reads one line from the file at a time.
- Use this when you want to read the file line by line.
Example:

```python
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='') 
        line = file.readline()
```
3. readlines()
- Reads the entire file and returns a list where each element is a line in the file.
- Use this when you want to process each line as a list element.
Example:

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='') 
```