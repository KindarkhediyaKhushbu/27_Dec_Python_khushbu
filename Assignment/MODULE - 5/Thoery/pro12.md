#####  Defining URLs and linking them to views.
- Django/DRF, URLs map client requests to views using urls.py.

📌 Example:
```python
from django.urls import path
from .views import student_list, StudentView

urlpatterns = [
    path('students/', student_list),        # FBV
    path('students-class/', StudentView.as_view()),  # CBV
]
```