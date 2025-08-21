##### Setting up the environment and installing necessary packages.
Create a Virtual Environment (keeps dependencies isolated)

python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows


Install Required Packages (like Django, Flask, DRF, etc.)

pip install django djangorestframework mysqlclient


Freeze Dependencies (so others can replicate the environment)

pip freeze > requirements.txt


Install from requirements (for teammates/servers)

pip install -r requirements.txt