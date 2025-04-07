### INF601 - Advanced Programming in Python
### Daniel Terreros
### Mini Project 4

# Mini Project 4

## Description

This project will be using django to create a 5 page project

## Getting Started

### Dependencies

```
pip install -r requirements.txt
```

### Initializing the Database

Before running the project, you need to set up the database:

1. **Create migration files**  
   This command creates SQL entries for any changes in your models:
```
python manage.py makemigrations
```

2. **Apply the migrations**  
This command applies the generated migrations to your database:
```
python manage.py migrate
```
3. **Create a superuser**  
This command sets up an administrator account for the Django admin site:
```
python manage.py createsuperuser
```

Follow the prompts to create your admin user.

### Running the Development Server

Once the database is set up, you can run the development server with:
```
python manage.py runserver
```



Then, open your browser and navigate to:
http://127.0.0.1:8000

### Notable additions
* An About us section
* An events section
* The ability to Login
* Register accounts using djangos built in registration system.



## Author

Daniel Terreros

## Acknowledgements
* [Django Login, Logout ](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
* [Register page usercreationform](https://dev.to/balt1794/registration-page-using-usercreationform-django-part-2-2fg)
* [Bootstrap](https://getbootstrap.com/)
* [Previous django project from awhile ago that helped me remember how to do some of this stuff!](https://github.com/DanielTKC/current_club)