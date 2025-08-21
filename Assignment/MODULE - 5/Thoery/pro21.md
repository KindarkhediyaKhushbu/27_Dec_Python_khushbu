##### Implementing authentication using Django REST Framework’s token-based system.

Implementing Token Authentication in DRF:

Install & Add App

pip install djangorestframework


settings.py → add 'rest_framework', 'rest_framework.authtoken'.

Migrate

python manage.py migrate


Enable Token Auth

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': [
      'rest_framework.authentication.TokenAuthentication',
  ]
}


Get Token URL

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ path('api/token/', obtain_auth_token) ]


Use in Views

class SecureView(APIView):
    permission_classes = [IsAuthenticated]


Client Usage

Get token → POST /api/token/ {username, password}

Use → Authorization: Token <token>