#### Accessing, adding, updating, and deleting dictionary elements

<b>1. Accessing :</b>
- You can access the value of a specific key by using square brackets [] or the .get() method.

```python
person = {
    "name": "khushbu",
    "age": 21,
    "city": "junagadh"
}

print(person["name"]) 
print(person.get("age")) 
```

<b>2. Adding:</b>
- You can add a new key-value pair by simply assigning a value to a new key.

```python
person["occupation"] = "It"
print(person) 
```

<b>3. Updating </b>
- To update an existing key, just assign a new value to that key.

```python
person["age"] = 26 
print(person)
```
<b>4. Deleting :</b>
- To remove a key-value pair, you can use the del keyword or the .pop() method.

- del removes the key-value pair permanently.
- .pop() removes a key and returns the corresponding value.

```python
del person["city"]
print(person) 
# pop
city = person.pop("occupation")
print(person)  
print(city)
```

