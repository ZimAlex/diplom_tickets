from django.db import models

import time


class Experiment(models.Model):
    strategy = models.IntegerField()
    info = models.CharField(max_length=7)
    name = models.CharField(max_length=20)
    taskList = models.CharField(max_length=9000)
    mistakeList = models.CharField(max_length=9000)
    lastTask = models.CharField(max_length=100)
    startTime = models.FloatField(verbose_name='Время начала эксперимента', default=time.clock())
    Time = models.FloatField(verbose_name='Время затраченное на эксперимент', default=time.clock())
    replay = models.BooleanField()
    mistake = models.BooleanField()

class Task(models.Model):
    task_user = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    level = models.IntegerField()
    quest = models.CharField(max_length=6, verbose_name='Задание')
    answer = models.CharField(max_length=6, verbose_name='Правильный ответ')
    checking = models.CharField(max_length=100, default='Не счастливый')
    startTime = models.FloatField(verbose_name='Время попадания на страницу', default=time.clock())


class Variant(models.Model):
    variant_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    variant = models.CharField(max_length=6, verbose_name='Ваш Ответ ', default="")
    check = models.CharField(max_length=100, default='Не счастливый')
    answerTime = models.FloatField(verbose_name='Время ответа', default=time.clock())
    time = models.FloatField(verbose_name='Затраченное время', default=time.clock())
# Create your models here.
