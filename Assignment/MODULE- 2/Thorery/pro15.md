####  Iterating over a dictionary using loops.

<b>1. Iterating key :</b>
- You can iterate over just the keys of the dictionary using a for loop.

```python
person = {
    "name": "khushbu",
    "age": 21,
    "city": "Junagadh",
    }

for key in person:
    print(key)
```

<b>2. Iterating Values :</b>
- If you want to iterate over just the values, you can use the .values() method.

```python

for value in person.values():
    print(value)
```