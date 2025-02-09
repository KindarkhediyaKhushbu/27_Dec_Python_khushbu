#### Anonymous functions (lambda functions)

- Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 

- we defined a lambda function(upper) to convert a string to its upper case using upper().

```python
s1 = 'hello python'

s2 = lambda func: func.upper()
print(s2(s1))
```