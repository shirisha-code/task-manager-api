# Task Manager API (Backend + Frontend)

## Features

* User Registration & Login (JWT Authentication)
* Role-Based Access Control (Admin & User)
* Task CRUD APIs (Create, Read, Update, Delete)
* Secure APIs with authentication
* Swagger API Documentation

##  Tech Stack

* Django
* Django REST Framework
* JWT Authentication
* SQLite / PostgreSQL

##  API Endpoints

### Auth

* POST /api/register/
* POST /api/login/

### Tasks

* GET /api/tasks/
* POST /api/tasks/
* PUT /api/tasks/{id}/
* DELETE /api/tasks/{id}/

##  Authentication

* Use Bearer Token in Authorization header

##  API Docs

* Swagger: /swagger/
* Redoc: /redoc/

##  Setup Instructions

```bash
git clone <your-repo-link>
cd project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

##  Scalability Notes

* Can scale using microservices architecture
* Add Redis caching for performance
* Use Docker for containerization
* Load balancing with NGINX

## Screenshots
* Authorization
* Frontend
* login_api
* login_response
* register_api
* register_response
* tasks_api
* tasks_response
* taks_get

##  Author
Shirisha
