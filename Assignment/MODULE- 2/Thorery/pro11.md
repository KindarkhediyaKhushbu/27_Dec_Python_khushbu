#### Basic operations with tuples: concatenation, repetition, membership
<b>1. Concatenation:</b>
- Concatenating two tuples involves joining them together to form a new tuple.

```python

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  
```

<b>2. Repetition:</b>
- You can repeat a tuple a specified number of times by using the repetition operator (*).

```python

tuple1 = (1, 2, 3)
result = tuple1 * 3
print(result)  
```
<b>3. Membership:</b>
- To check if an element is present in a tuple, you can use the in keyword. It returns True if the element is found, otherwise False.

```python
tuple1 = (1, 2, 3, 4)
print(2 in tuple1)  
print(5 in tuple1) 
```