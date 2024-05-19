# -*- coding: utf-8 -*-
from rest_framework import serializers

from todoapp.backend.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created', 'completed']
        read_only_fields = ['created', 'completed']


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created', 'completed']
