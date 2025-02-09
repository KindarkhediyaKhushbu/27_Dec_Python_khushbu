#### Creating custom modules

1. Create a Custom Module
Create a Python file (math_operations.py) with functions:

```python
# math_operations.py
def add(a, b):
    return a + b
# 2. Use the Custom Module
import math_operations
result = math_operations.add(5, 3)
print(result)  
# 3. Run the Code
import math_operations as mo
print(mo.subtract(10, 4))  
```