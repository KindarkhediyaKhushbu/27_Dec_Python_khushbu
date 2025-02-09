#### Understanding list methods like append(), insert(), remove(), pop().

<b>append()</b>
- Adds an element to the end of a list.
- Example:
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```
<b>insert():</b>

- Adds an element at a specific position in the list.
- It takes two arguments: the index where the element should be inserted and the element itself.
- Example:
```python
my_list = [1, 2, 3]
my_list.insert(1, 10)  
print(my_list)
```
<b>remove():</b>

- Removes the first occurrence of a specified value from the list.
- Example:
```python

my_list = [1, 2, 3, 2]
my_list.remove(2)  
print(my_list)
```

<b>pop():</b>

- Removes and returns the element at a specified index (default is the last item).

- Example:
```python
my_list = [1, 2, 3]
popped_element = my_list.pop()  
print(popped_element)  
print(my_list)
```