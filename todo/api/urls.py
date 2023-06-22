from django.urls import path
from todo.api import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo-list'),
    path('todo/<int:pk>', views.todo_details, name='todo_details'),
]
