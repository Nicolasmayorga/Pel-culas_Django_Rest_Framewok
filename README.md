## Movie's API REST

This repositorie include a REST API of movies construct in Django and Django Rest framework. Include all Http protocles, his local host, Token system for authentication and integration and dockerfile for dockerization for a future deploy in AWS, Heroku, Azure or any system.

## Basic requiremenst

- Django==3.1.4
- django-allauth==0.44.0
- django-import-export==2.4.0
- django-rest-auth==0.9.5
- djangorestframework==3.12.2
- Markdown==3.3.3

## Recomendations
Use a env for make interation with the API Rest

## Folders and files

This API content 2 folders that content the structure of the project.

# api_pelis
In the folder api_pelis you can show the fundamental structure of the API. The principal changes of these are in the file settings.py In this file you can show all the aplications that are include for the API. The basoic of django project, the django rest framework and authorization, import_export for transform the database in a file cvs or impor with querys to the database sice the admin.

Also the settings include the portocles of authentication in the backend. Make the email and not the username the principal state for login.

In the file urls.py we structure the endpoint for make a interactions and authentication of the api. You can add a movie, make it your favorite and delete part of the database if you are superuser.

# api

In the app api we structure of the API REST trougth the model of django MTV (Model Template View).

We initiate with the model. We create a simple model of movies for structurate the database of our API. Also, we create a fuction that allow to the user indicate his favorite movis and these gonna be reflected in the database doing the migrations. 

AS second point we create the serializer of the API for reflect our model as a query and make it rest and allows the interaction in queries to the user or to the fron end.

Finally, we create the views of the API. In this we connected with the views of our projhect for allows the login, the signup, add movies, delete and edit movies if are superuser. 


## Instructions

For make a interaction wit the API

1. Activate your env of the app

2. Run the localhost in the terminal with the command in your terminal: python manage.py run server
You can go to your web navigator and go to the link http://localhost:8000/

3. For see the database in queries you can go to the link:  http://localhost:8000/api/v1/ 

4. For make a interaction with the API REST you need singnup. you can do it these trougth the terminal with curl or same goinf to the login.

Note: If you wanna make login with the superuser to access to the you can go to  http://localhost:8000/admin The credential are: 
email: nmayorgav@gmail.com
password admin123456

6. You cad add a new movie between the the admin or between curl in the console with this token and give it the query of the move.

curl -X POST http://127.0.0.1:8000/api/v1/ -H "Authorization: Token a060455bb08a203cd6ce51c7f46190b43cd828b3"

Also you can add a movie import a cvs file with the correct query or same in the template generate it by django api_rest framework if you are authenticate it.


enjoy it !!