# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок задачи")  # task title
    memo = models.TextField(blank=True, verbose_name="Описание")  # description
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # set current time
    completed = models.BooleanField(default=False, verbose_name="Статус выполнения")  # task completed status

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
