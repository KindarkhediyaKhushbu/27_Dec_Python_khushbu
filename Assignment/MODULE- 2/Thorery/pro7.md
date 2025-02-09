#### Sorting and reversing a list using sort(), sorted(), and reverse().

<b>1. Using sort():</b>
- The sort() method sorts the list in-place, meaning it modifies the original list and does not return a new list.

```python
list = [5, 2, 9, 1, 5, 6]
list.sort()
print(list)
```
<b>2. Using sorted():</b>
- The sorted() function works similarly to sort(), but it returns a new sorted list without modifying the original one.

```python

list = [5, 2, 9, 1, 5, 6]

sorted_list = sorted(list)
print(sorted_list)
print(list)  
```

<b>3. Using reverse()</b>:
- The reverse() method reverses the elements of the list in-place, meaning it modifies the original list.

```python

list = [5, 2, 9, 1, 5, 6]
list.reverse()
print(list)
```