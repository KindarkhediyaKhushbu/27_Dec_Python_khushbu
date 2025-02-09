#### Dictionary methods like keys(), values(), and items().

<b>1. keys() Method:</b>
- Purpose: Returns a view object that displays a list of all the keys in the dictionary.
- Usage: Useful when you want to iterate over or check the keys of a dictionary.

```python
person = {
    "name": "khushbu",
    "age": 2`,
    "city": "junagadh"
}
keys = person.keys()
print(keys)  
keys_list = list(keys)
print(keys_list)  
```
<b>2. values() Method:</b>
- Purpose: Returns a view object that displays a list of all the values in the dictionary.
- Usage: Useful when you want to access or iterate over the values in the dictionary.

```python

values = person.values()
print(values)  
values_list = list(values)
print(values_list) 
```
<b>3. items() Method:</b>
- Purpose: Returns a view object that displays a list of tuples, each containing a key-value pair from the dictionary.
- Usage: Helpful when you want to work with both keys and values together.

```python
items = person.items()
print(items)  
items_list = list(items)
print(items_list) 
```