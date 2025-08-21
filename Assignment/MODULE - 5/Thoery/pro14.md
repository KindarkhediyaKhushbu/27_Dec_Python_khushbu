##### Configuring Django settings for database, static files, and API keys.
Database → Configure in DATABASES:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Static Files →
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]


API Keys / Secrets → Store in .env (using python-decouple or os.environ):

import os
API_KEY = os.getenv("API_KEY")
```