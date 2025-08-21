##### Adding pagination to APIs to handle large data sets.
- DRF, enable pagination by setting a pagination class in settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```