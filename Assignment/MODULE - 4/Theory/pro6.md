##### Linking external or internal JavaScript files in Django. 
-  Django, linking JavaScript files—whether external or internal—requires understanding 
how Django handles static files and template rendering.  
###### 1. Set Up Static Files 
- Ensure your Django project is configured to serve static files: 
- In your settings.py file: 
STATIC_URL = '/static/'  
STATICFILES_DIRS = [BASE_DIR / "static"] 
- Create a static directory in your project root or app directories. For example: 
project_root/ 
static/ 
js/  
script.js 
###### 2. Linking Internal JavaScript Files 
- To link JavaScript files stored in your static directory: 
1. Load Static Files in Templates 
At the top of your template, load the static template tag: 
{% load static %} 
2. Include the JavaScript File 
Use the static tag to reference your file: 
<script src="{% static 'js/script.js' %}"></script> 
3. Linking External JavaScript Files 
To include an external JavaScript file, directly add the


 <script> tag with the file's URL: 
<script src="https://cdn.example.com/library.js"></script> 
4. Using JavaScript in a Django Template 
Here's an example of a full Django template: 

```python
<!DOCTYPE html> 
<html lang="en"> 
<head> 
<meta charset="UTF-8"> 
<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
<title>Django JavaScript Example</title> 
{% load static %} 
<script src="{% static 'js/script.js' %}"></script> 
</head> 
<body> 
<h1>Hello, Django!</h1> 
<button id="myButton">Click Me</button> 
</body> 
</html> 
```
###### 5. Collect Static Files for Deployment 
- When deploying, use Django's collectstatic management command to gather all static files into the 
- directory defined by STATIC_ROOT. 
python manage.py collectstatic 
Ensure your web server (e.g., Nginx) is - - - - configured to serve files from the STATIC_ROOT 
directory. 
{% block %} and {% extends %} tags to manage JavaScript in a base template for 
consistency across pages. 
's JsonResponse and AJAX.