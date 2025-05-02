#### Generating dynamic HTML content using Django templates.

- Static files are files that don’t change dynamically, such as CSS, JavaScript, and image
files. Django provides built-in support to manage static files efficiently using the
django.contrib.staticfiles app.
- Configuring STATIC_URL and STATICFILES_DIRS
In the settings.py file, configure the following settings to define how Django should locate and
serve static files:
<b>STATIC_URL:</b> This defines the URL prefix for accessing static files.
- Example:
STATIC_URL = '/static/'

<b> STATICFILES_DIRS:</b> This setting tells Django where to look for additional static files in
your project directory structure (other than the default app_name/static directories).
STATICFILES_DIRS = [
 BASE_DIR / "static",
]
- Organizing Static Files
Django uses a specific directory structure to locate static files:
- Place app-specific static files in a static directory inside each app.
- For example:
myapp/
 static/
 myapp-
 style.css
- For project-wide static files, use a global static directory (as configured in
STATICFILES_DIRS).
- Using the collectstatic Command
In a production environment, Django collects all static files into a single location specified by the
STATIC_ROOT setting. This is achieved using the collectstatic management command.
- Configure STATIC_ROOT in settings.py:
STATIC_ROOT = BASE_DIR / "staticfiles"
- Run the command:
python manage.py collectstatic
This command consolidates all static files into the STATIC_ROOT directory for efficient serving
by a web server.
- Serving Static Files
- Development: During development, Django automatically serves static files when DEBUG
is set to True. The runserver command takes care of this, so you don’t need additional
configuration.
- Production: In production, Django doesn’t serve static files. Use a dedicated web server
like Nginx or Apache to serve files from the STATIC_ROOT directory. These servers are
optimized for handling static file requests.
- Referencing Static Files in Templates
Use the {% static %} template tag to reference static files in templates.
```python
Example:
<link rel="stylesheet" href="{% static 'myapp/style.css' %}">
<script src="{% static 'myapp/script.js' %}"></script>
```
- Enabling the Static Files App
Ensure that django.contrib.staticfiles is included in the INSTALLED_APPS list in settings.py.
This app provides tools for managing static files.
Summary
- Configure STATIC_URL, STATICFILES_DIRS, and STATIC_ROOT in settings.py.
 Organize files in static directories within apps or globally.
- manage and serve static files in a Django project.
