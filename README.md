# Simple-shop
Simple Django admin panel  and ordering system


![Default Home View](__screenshots/dashboard.png?raw=true "Title")

### Main features

* Separated dev and production settings

* Example app with custom user model

* Bootstrap static files included

* User registration and logging in

* Separated requirements files

* Filtering orders

* Use Category to see specific Orders


# Getting Started
To use this template to start your own project:

clone the project

    git clone https://github.com/amirhossein-bayati/Simple-shop.git
    
create and start a a virtual environment

    virtualenv env --no-site-packages

    source env/bin/activate

Install the project dependencies:

    pip install -r requirements.txt

create admin account

    python manage.py createsuperuser
      
then

    python manage.py makemigrations

to makemigrations for the app

then again run

    python manage.py migrate

to start the development server

    python manage.py runserver

and open localhost:8000 on your browser to view the app.
