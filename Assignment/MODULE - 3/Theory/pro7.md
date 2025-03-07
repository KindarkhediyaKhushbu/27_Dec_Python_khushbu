#### Closing files using close().

- The close() method closes an open file.

- ou should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

```python

file = open('example.txt', 'w')
file.write("This is a test file.")

file.close()
```