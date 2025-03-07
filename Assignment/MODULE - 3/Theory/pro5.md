#### Opening files in different modes ('r', 'w', 'a', 'r+', 'w+').

##### ‘a’
- In ‘a’ mode, the file is opened for writing, positioned at the end if it exists, creates a new empty file if not, appends data without altering existing content, and disallows reading.

```python
with open('example.txt', 'a') as file:
    file.write('Appended text\n')
```
##### ‘w’
- It opens the file for writing. If the file exists, it truncates (clears) its content. If the file doesn’t exist, Python creates a new, empty file. Reading from the file is not allowed in this mode.

```python
with open('example.txt', 'w') as file:
    file.write('This will overwrite existing content')
```
##### ‘r’
- This code segment opens a file named ‘file_r.txt’ in ‘read’ mode (‘r’). It then reads the content of the file using the .read() method and stores it in the variable content. The ‘r’ mode is used for reading files, and it will raise a FileNotFoundError if the file does not exist.

```python
with open('example.txt', 'r') as file_r:
    content = file_r.read()
    print('Content in "r":', content)
```
##### ‘r+’
- In ‘r+’ mode, the file is opened for both reading and writing without truncation, and the file pointer is positioned at the beginning. If the file doesn’t exist, a FileNotFoundError is raised.

```python
with open('example.txt', 'r+') as file:
    content = file.read()
    print(content)
    file.write('Appending new content')
```
Write and Read Mode in Python with ‘w+’
In ‘w+’ mode, the file is opened for both reading and writing, existing content is cleared, a new empty file is created if it doesn’t exist, and the file pointer is positioned at the beginning.

```python
with open('example.txt', 'w+') as file:
    file.write('This will overwrite existing content')
    content = file.read()
    print(content)
```