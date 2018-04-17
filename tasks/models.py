#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

import datetime


class Experiment(models.Model):
    Strategy = models.IntegerField(null=True, blank=True)
    Info = models.CharField(max_length=7, null=True, blank=True)
    Name = models.CharField(max_length=20, null=True, blank=True)
    TaskList = models.CharField(max_length=9000, null=True, blank=True)
    MistakeList = models.CharField(max_length=9000)
    LastTask = models.CharField(max_length=100)
    StartTime = models.TimeField(default=datetime.datetime.now())
    EndTime = models.TimeField(default=datetime.datetime.now())
    Timing = models.IntegerField()
    Replay = models.BooleanField()
    Mistake = models.BooleanField()


class Task(models.Model):
    Task_user = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    Level = models.IntegerField(null=True, blank=True)
    Quest = models.CharField(max_length=6, verbose_name='Задание', null=True, blank=True)
    Answer = models.CharField(max_length=6, verbose_name='Правильный ответ', null=True, blank=True)
    Checking = models.CharField(max_length=100, default='Не счастливый', null=True, blank=True)
    StartTime = models.TimeField(default=datetime.datetime.now())


class Variant(models.Model):
    Variant_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    Variant = models.CharField(max_length=6, verbose_name='Ваш Ответ ', default="", null=True, blank=True)
    Check = models.CharField(max_length=100, default='Не счастливый', null=True, blank=True)
    AnswerTime = models.TimeField(default=datetime.datetime.now())
    Time = models.IntegerField()
# Create your models here.
