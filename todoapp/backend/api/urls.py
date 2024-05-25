# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.TodoListView.as_view(), name='todo-list'),
    path('todos/create/', views.TodoListCreate.as_view(), name='todo-create'),
    path('todos/<int:pk>/', views.TodoRetrieveUpdateDestroy.as_view(), name='todo-CRUD'),
    path('todos/<int:pk>/complete/', views.TodoToggleComplete.as_view(), name='todo-toggle-complete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
