#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

import time


class Experiment(models.Model):
    Strategy = models.IntegerField(null=True, blank=True)
    Info = models.CharField(max_length=7, null=True, blank=True)
    Name = models.CharField(max_length=20, null=True, blank=True)
    TaskList = models.CharField(max_length=9000, null=True, blank=True)
    MistakeList = models.CharField(max_length=9000, null=True, blank=True)
    LastTask = models.CharField(max_length=100, null=True, blank=True)
    StartTime = models.FloatField(verbose_name='Время начала эксперимента', default=time.clock(), null=True, blank=True)
    Timing = models.FloatField(verbose_name='Время затраченное на эксперимент', default=time.clock(), null=True, blank=True)
    Replay = models.BooleanField()
    Mistake = models.BooleanField()


class Task(models.Model):
    Task_user = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    Level = models.IntegerField(null=True, blank=True)
    Quest = models.CharField(max_length=6, verbose_name='Задание', null=True, blank=True)
    Answer = models.CharField(max_length=6, verbose_name='Правильный ответ', null=True, blank=True)
    Checking = models.CharField(max_length=100, default='Не счастливый', null=True, blank=True)
    StartTime = models.FloatField(verbose_name='Время попадания на страницу', default=time.clock(), null=True, blank=True)


class Variant(models.Model):
    Variant_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    Variant = models.CharField(max_length=6, verbose_name='Ваш Ответ ', default="", null=True, blank=True)
    Check = models.CharField(max_length=100, default='Не счастливый', null=True, blank=True)
    AnswerTime = models.FloatField(verbose_name='Время ответа', default=time.clock(), null=True, blank=True)
    Time = models.FloatField(verbose_name='Затраченное время', default=time.clock(), null=True, blank=True)
# Create your models here.
