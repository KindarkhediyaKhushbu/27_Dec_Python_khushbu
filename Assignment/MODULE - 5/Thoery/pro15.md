##### • Setting up a Django REST Framework project.
- Steps to set up DRF project:

1. Install: pip install django djangorestframework

2. Create project & app: django-admin startproject myproject, python manage.py startapp api

3. Add 'rest_framework' & 'api' to INSTALLED_APPS

4. Define models, create serializers, add views

5. Map URLs with path('api/', include('api.urls'))

6. Run server: python manage.py runserver
