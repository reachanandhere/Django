# Creating a virtual env on MAC
1. pip3 install --user virtualenv
2. python3.12 -m venv venv
3. source venv/bin/activate

# Once the Virtual environment is setup
# Inside it, install django
1. pip3 install django

# To run Django Server
1. django-admin startproject [projectname]
2. cd [projectname]
3. python3 manage.py runserver