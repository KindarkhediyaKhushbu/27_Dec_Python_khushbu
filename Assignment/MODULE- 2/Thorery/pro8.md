#### Basic list manipulations: addition, deletion, updating, and slicing.

<b>1. Deletion (Remove, Pop, Del)</b>
- Remove: Removes the first occurrence of the specified element.

```python
list = [1, 2, 3, 2]
list.remove(2) 
print(list) 
# pop
list.pop(2)
peint(list)
# del
list.del(2)
print(list)
```

<b>2. Updating (Modify an Element)</b>
- You can directly modify an element using its index.

```python
list = [1, 2, 3]
list[1] = 5  
print(list)  
```
<b>3. Slicing</b>
- Slicing allows you to extract a sublist by specifying a range of indices.

```python
list = [1, 2, 3, 4, 5]
sublist = list[1:4]  
print(sublist) 
```

<b>4. Addition (Append, Insert)</b>
- Appending: Adds an element to the end of the list.

```python

list = [1, 2, 3]
list.append(4)  
print(list)  
# insert
list.insert(5)
print(list)
```