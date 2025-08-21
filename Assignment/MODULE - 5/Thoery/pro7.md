##### Converting Django QuerySets to JSON
- in Django, QuerySets (collections of model objects) aren’t directly JSON serializable. To send them in an API response or use them in JavaScript, you need to convert QuerySets to JSON.



- 1. Using Django’s Built-in Serializer
from django.core import serializers
from django.http import JsonResponse
from .models import Student

```python
def student_list(request):
    students = Student.objects.all()
    data = serializers.serialize("json", students)
    return JsonResponse(data, safe=False)
```