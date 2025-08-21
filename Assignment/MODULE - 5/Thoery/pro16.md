##### • Implementing social authentication (e.g., Google, Facebook) in Django.

###### Steps to Implement Social Authentication in Django

- Install required package

- pip install social-auth-app-django

```python
Add to Installed Apps (settings.py)

INSTALLED_APPS = [
    ...
    'social_django',
]


Update Authentication Backends (settings.py)

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',    # For Google
    'social_core.backends.facebook.FacebookOAuth2',# For Facebook
    'django.contrib.auth.backends.ModelBackend',   # Default
)


Add Social Auth Settings (settings.py)

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-google-client-id'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-google-client-secret'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = 'your-facebook-app-id'
SOCIAL_AUTH_FACEBOOK_SECRET = 'your-facebook-app-secret'

LOGIN_REDIRECT_URL = '/'   # After login success
LOGOUT_REDIRECT_URL = '/'  # After logout


Add URLs (urls.py)

from django.urls import path, include

urlpatterns = [
    ...
    path('oauth/', include('social_django.urls', namespace='social')),
]


Run Migrations

python manage.py migrate


Add Login Buttons in Template

<a href="{% url 'social:begin' 'google-oauth2' %}">Login with Google</a>
<a href="{% url 'social:begin' 'facebook' %}">Login with Facebook</a>
```1