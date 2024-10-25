# Helpful Commands
-------------------
-------------------
-------------------
# Commands: General Navigation
cd . . 
    *this moves us back a directory


--------------------
-------------------
-------------------
# Commands: Django

python -m venv NAME_OF_ENVIROMENT
    *this creates a django enviroment. You should follow this by activating the enviroment.

NAME_OF_ENVIROMENT\Scripts\activate
    *this activates the enviroment. Turn it off by typing in deactivate. Onced activated you should make sure django is installed.

pip install django
    *this installs

django-admin startproject NAME_OF_APP
    *this must be done within the django enviroment and with it installed. 

python manage.py migrate
    *this creates a SQL database. For me it created db.sqlite3

python manage.py runserver
    *runs the server. You can exit by pressing CTRL+C 