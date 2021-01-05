# Stark
1] First Create Projects by using this command,
  django-admin startproject Test

2] Goto insode the project and add the app using this command,
  python manage.py startapp app

3] Write into the settings.py file inside the 
  INSTALLED_APPS = [
    'app',
    'rest_framework',
    'rest_framework.authtoken',
  ]

4] Write inside the models.py file


5] Write the command in terminal
  python manage.py makemigrations
  python manage.py migrate

6] Create superuser using this command,
  python manage.py createsuperuser

7] Run the project using this command 
  python manage.py runserver

 
