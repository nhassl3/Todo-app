# -*- coding: utf-8 -*-
from rest_framework import generics, permissions
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from todoapp.backend.api.serializers import TodoSerializer, TodoToggleCompleteSerializer
from todoapp.backend.todo.models import Todo

__all__ = ['TodoListCreate', 'TodoListView', 'TodoRetrieveUpdateDestroy', 'TodoToggleComplete', 'signup', 'login']


class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by("created")  # type: ignore


class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created')  # type: ignore

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)  # type: ignore


class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)  # type: ignore

    def perform_update(self, serializer):
        serializer.instance.completed = not serializer.instance.completed
        serializer.save()


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()
            token = Token.objects.create(user=user)  # type: ignore
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'User already exists'}, status=400)


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        user = authenticate(
            username=data['username'], password=data['password']
        )
        if user is None:
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
        try:
            token = Token.objects.get(user=user)  # type: ignore
        except:
            token = Token.objects.create(user=user)  # type: ignore
        return JsonResponse({'token': str(token)}, status=201)
    