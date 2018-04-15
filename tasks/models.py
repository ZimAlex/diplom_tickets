#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

import time


class Experiment(models.Model):
    strategy = models.IntegerField(null=True, blank=True)
    info = models.CharField(max_length=7,null=True, blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    taskList = models.CharField(max_length=9000, null=True, blank=True)
    mistakeList = models.CharField(max_length=9000, null=True, blank=True)
    lastTask = models.CharField(max_length=100, null=True, blank=True)
    startTime = models.FloatField(verbose_name='Время начала эксперимента', default=time.clock(), null=True, blank=True)
    time = models.FloatField(verbose_name='Время затраченное на эксперимент', default=time.clock(), null=True, blank=True)
    replay = models.BooleanField()
    mistake = models.BooleanField()


class Task(models.Model):
    task_user = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    level = models.IntegerField(null=True, blank=True)
    quest = models.CharField(max_length=6, verbose_name='Задание', null=True, blank=True)
    answer = models.CharField(max_length=6, verbose_name='Правильный ответ', null=True, blank=True)
    checking = models.CharField(max_length=100, default='Не счастливый', null=True, blank=True)
    startTime = models.FloatField(verbose_name='Время попадания на страницу', default=time.clock(), null=True, blank=True)


class Variant(models.Model):
    variant_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    variant = models.CharField(max_length=6, verbose_name='Ваш Ответ ', default="", null=True, blank=True)
    check = models.CharField(max_length=100, default='Не счастливый', null=True, blank=True)
    answerTime = models.FloatField(verbose_name='Время ответа', default=time.clock(), null=True, blank=True)
    time = models.FloatField(verbose_name='Затраченное время', default=time.clock(), null=True, blank=True)
# Create your models here.
