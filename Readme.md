# Todo Api Project Documentation

This project is a Django REST API application that manages Todos and Categories. It provides endpoints for creating, listing, updating, and deleting Todos and Categories. The project uses Django, Django REST framework, and PostgreSQL.

-----------------------------------------------------------------------

## Endpoints

### Todos

- `POST /todos`: Create a new Todo
- `GET /list_todos`: List all Todos
- `GET /todos/<todo_id>/`: Get details of a specific Todo
- `PUT /todos/<todo_id>/update`: Update a Todo
- `DELETE /todos/<todo_id>/delete`: Delete a Todo

### Categories

- `POST /create/`: Create a new Category
- `GET /list/`: List all Categories
- `GET /details/<category_id>/`: Get details of a specific Category
- `PUT /update/<category_id>/`: Update a Category
- `DELETE /delete/<category_id>/`: Delete a Category

## Models

### Category

- `name`: CharField (max_length=50)
- `description`: TextField

### Todo

- `title`: CharField (max_length=100)
- `description`: TextField
- `created_at`: DateTimeField (auto_now_add=True)
- `due_date`: DateField
- `priority`: CharField (choices=['Low', 'Medium', 'High'])
- `completed`: BooleanField (default=False)
- `category`: ForeignKey to Category (on_delete=models.CASCADE, related_name='todos', null=True, blank=True)

## Views Documentation

### Todo Views

- `create_todo`: View to create a new Todo. Accepts POST requests.
- `list_todos`: View to list all Todos. Accepts GET requests.
- `get_todo_details`: View to get details of a specific Todo. Accepts GET requests.
- `update_todo`: View to update a Todo. Accepts PUT requests.
- `delete_todo`: View to delete a Todo. Accepts DELETE requests.

### Category Views

- `create_category`: View to create a new Category. Accepts POST requests.
- `list_categories`: View to list all Categories. Accepts GET requests.
- `get_category_details`: View to get details of a specific Category. Accepts GET requests.
- `update_category`: View to update a Category. Accepts PUT requests.
- `delete_category`: View to delete a Category. Accepts DELETE requests.



## Structure

The project follows a typical Django project structure with the following components:

- `base`: Contains the main Django app for the project.
  - `admin.py`: Configuration for Django admin panel.
  - `apps.py`: Configuration for Django app.
  - `models.py`: Contains the database models for Category and Todo.
  - `serializers.py`: Contains serializers for Category and Todo models.
  - `tests.py`: Contains tests for the app.
  - `urls.py`: Contains URL patterns for the app.
  - `views.py`: Contains views for the app.
  - `__init__.py`: Initialization file for the app.

  - `api`: Subdirectory containing API views for Category and Todo.
    - `category.py`: Contains API views for Category model.
    - `todo.py`: Contains API views for Todo model.

- `migrations`: Contains database migration files.
- `__pycache__`: Contains Python cache files.

- `TodoApi`: Main project directory.
  - `asgi.py`: ASGI configuration.
  - `settings.py`: Django project settings.
  - `urls.py`: Main URL configuration.
  - `wsgi.py`: WSGI configuration.
  - `__init__.py`: Initialization file for the project.

```bash
│   db.sqlite3
│   manage.py
│   Readme.md
│
├───base
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   serializers.py
│   │   tests.py
│   │   urls.py
│   │   __init__.py
│   │
│   ├───api
│   │   │   category.py
│   │   │   todo.py
│   │   │
│   │   └───__pycache__
│   │           category.cpython-311.pyc
│   │           todo.cpython-311.pyc
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           0001_initial.cpython-311.pyc
│   │           __init__.cpython-311.pyc
│   │
│   └───__pycache__
│           admin.cpython-311.pyc
│           apps.cpython-311.pyc
│           models.cpython-311.pyc
│           serializers.cpython-311.pyc
│           url.cpython-311.pyc
│           urls.cpython-311.pyc
│           views.cpython-311.pyc
│           __init__.cpython-311.pyc
│
└───TodoApi
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py
    │
    └───__pycache__
            settings.cpython-311.pyc
            urls.cpython-311.pyc
            wsgi.cpython-311.pyc
            __init__.cpython-311.pyc
```