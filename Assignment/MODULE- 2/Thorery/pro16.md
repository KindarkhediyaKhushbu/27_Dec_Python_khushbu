#### Merging two lists into a dictionary using loops or zip().

- Iterate through both lists simultaneously using zip and for each pair, add the first element as the key and second as the value to the dictionary.

```python

a = ["name", "age", "city"]
b = ["Alice", 30, "New York"]
res = {}
7
for key, value in zip(a, b):
    res[key] = value
print(res)
```