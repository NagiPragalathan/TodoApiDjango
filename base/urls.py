from django.contrib import admin
from django.urls import path
from .api.todo import create_todo, list_todos, get_todo_details, update_todo, delete_todo
from .api.category import create_category, list_categories, get_category_details, update_category, delete_category

urlpatterns=[]

todo_urls = [
    path('todos', create_todo, name='todo-create'),
    path('list_todos', list_todos, name='list_todos'),
    path('todos/<int:todo_id>/', get_todo_details, name='todo-details'),
    path('todos/<int:todo_id>/update', update_todo, name='todo-update'),
    path('todos/<int:todo_id>/delete', delete_todo, name='todo-delete'),
]


category_urls = [
    path('create/', create_category, name='create_category'),
    path('list/', list_categories, name='list_categories'),
    path('details/<int:category_id>/', get_category_details, name='get_category_details'),
    path('update/<int:category_id>/', update_category, name='update_category'),
    path('delete/<int:category_id>/', delete_category, name='delete_category'),
]

urlpatterns.extend(todo_urls)
urlpatterns.extend(category_urls)

