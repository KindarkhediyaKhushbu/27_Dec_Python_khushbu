#### 

- Given a string, the task is to write a program in Python that prints the number of occurrences of each character in a string. There are multiple ways in Python, we can do this task. Let’s discuss a few of them. 

```python

ef count_characters(s):
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


input_string = "apple"
result = count_characters(input_string)
print(result)
```