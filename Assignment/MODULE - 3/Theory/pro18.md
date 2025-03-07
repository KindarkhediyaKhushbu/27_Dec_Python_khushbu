#### Using re.search() and re.match() functions in Python’s re module for pattern matching.

<b>re.search():</b>
- Description: The re.search() function searches the entire string for a match to the pattern and returns a match object if found. It does not require the match to be at the beginning of the string.
- Usage: It returns a match object if there’s a match anywhere in the string, otherwise it returns None.

```python
import re

x = "This is Python!"

result = re.search("Python", x)
# print(result)

if result:
    print("Match Done...")
else:
    print("Error!")
```
<b>re.match():</b>
Description: The re.match() function checks if the pattern matches only at the beginning of the string. If the match is found at the start, it returns a match object. If the match is not at the beginning, it returns None.

```python
import re

text = "The quick brown fox jumps over the lazy dog"

pattern = r"The"
match = re.match(pattern, text)

if match:
    print(f"Match found: {match.group()}")
else:
    print("Pattern not found at the beginning")
```ss