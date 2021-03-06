#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect, render

from numpy import median as med
from numpy import average as avg
from .models import Experiment, Task, Variant
from . import generator
from .forms import VariantForm
from django.template.context_processors import csrf
import time
import random


def generate(request):
    r = random.randint(1,8)
    r = 5
    c = random.randint(0,1)
    # c = 0
    if r == 7 or r == 8:
        c = 0
    if c == 1:
        inf = 'Открыто'
    else:
        inf = 'Закрыто'

    if r == 7:
        repl = True
    else:
        repl = False
    exp = Experiment(
        Replay=repl,
        Info=inf,
        Strategy=r,
        Mistake=False,
        Name=request.user
    )
    exp.save(force_insert=True)
    g = generator.read()
    for lev in range(0, len(g)):
        for key in (g[lev]):
            t = Task(
                Task_user=exp,
                Level=lev+1,
                Quest=key,
                Answer=g[lev][key],
            )
            t.save(force_insert=True)
    return redirect('/tasks/intro')


def main(request):
    exp = Experiment.objects.get(Name=request.user)
    exp.StartTime = time.time()
    exp.save()
    args = {}
    args['strategy'] = exp.Strategy
    return render_to_response('tasks/mainPage.html', args)


def createList(request):
    l = []
    exp = Experiment.objects.get(Name=request.user)
    strategy = exp.Strategy
    for t in Task.objects.filter(Task_user=Experiment.objects.get(Name=request.user)):
        l.append(str(t.id))
    if strategy == 5:
        l.reverse()
    elif strategy == 6:
        random.shuffle(l)
    exp = Experiment.objects.get(Name=request.user)
    exp.TaskList = ','.join(l)
    exp.save(force_insert=False)
    return redirect('/tasks/task/%s' % l[0])


def getTask(request, task_id):

    variant_form = VariantForm
    exp = Experiment.objects.get(Name=request.user)
    if exp.Mistake:
        tl = exp.MistakeList.split(',')
    else:
        tl = exp.TaskList.split(',')
    ml = []

    #
    # if  exp.Strategy != 8 and tl.index(task_id) == len(tl)-1:   #posible error
    #     if exp.Replay and not exp.Mistake:
    #         for id in tl:
    #             task = Task.objects.get(id=id)
    #             if task.Checking != 'Решено':
    #                 ml.append(id)
    #         exp.MistakeList = ','.join(ml)
    #         exp.Mistake = True
    #         exp.save()
    #         return redirect('/tasks/mistakes/%s' % ml[0])
    #     else:
    #         return redirect('/tasks/finalPage')
    args = {}
    args.update(csrf(request))
    args['task'] = Task.objects.get(id=task_id)
    args['form'] = variant_form
    t = Task.objects.get(id=task_id)
    t.StartTime = time.time()
    t.save()
    tList = exp.TaskList.split(',')
    if exp.Mistake:
        mList = exp.MistakeList.split(',')
    if exp.Info == "Открыто":
        if not exp.Mistake and str(int(task_id)-1) in tList:
            t2 = Task.objects.get(id=str(int(task_id)-1))
            args['check'] = t2.Checking
        elif exp.Mistake and str(int(task_id)-1) in mList:
            t2 = Task.objects.get(id=str(int(task_id) - 1))
            args['check'] = t2.Checking
        return render_to_response('tasks/task_cl_2.html', args)
    return render_to_response('tasks/task_cl.html', args)

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def addVariant_cl(request, task_id):
    if request.POST:
        form = VariantForm(request.POST)
        if form.is_valid():
            t = Task.objects.get(id=task_id)
            var = form.save(commit=False)

            var.Variant_task = Task.objects.get(id=task_id)
            nums = str(var.Variant)
            try:
                s1 = int(nums[0]) + int(nums[1]) + int(nums[2])
                s2 = int(nums[3]) + int(nums[4]) + int(nums[5])
            except IndexError:
                args = {}
                args['error'] = 'Введите корректный номер билета (6 цифр)'
                args['task_id'] = "/tasks/" + str(task_id)
                return render_to_response("tasks/error.html", args)
            except ValueError:
                args = {}
                args['error'] = 'Введите номер следующего счастливого билета'
                args['task_id'] = "/tasks/" + str(task_id)
                return render_to_response("tasks/error.html", args)


            if s1 == s2 and var.Variant != Task.objects.get(id=task_id).Answer:
                var.Check = 'Счастливый, но не ближайший'
                t.Checking = 'Счастливый, но не ближайший'
            elif var.Variant == Task.objects.get(id=task_id).Answer:
                var.Check = 'Решено'
                t.Checking = 'Решено'
            else:
                var.Check = Variant.Check
            var.AnswerTime = time.time()
            # var.time = var.answerTime - t.startTime
            delta = var.AnswerTime - t.StartTime
            var.Time = round(delta, 2)
            if t.Ans_number == 0:
                t.var_time1 = var.Time
            elif t.Ans_number == 1:
                t.var_time2 = var.Time
            elif t.Ans_number == 2:
                t.var_time3 = var.Time
            t.Ans_number += 1
            t.save()
            form.save()
    exp = Experiment.objects.get(Name=request.user)
    tl = exp.TaskList.split(',')
    if exp.Mistake:
        check = True
    else:
        check = tl.index(task_id) == 2 or tl.index(task_id) == 5 or tl.index(task_id) == 8 or tl.index(task_id) == 11 or tl.index(task_id) == 14 or tl.index(task_id) == 17
    if exp.Strategy == 8 and check:

        if not exp.Mistake:

            if tl.index(task_id) == 2:
                lev = 1
            elif tl.index(task_id) == 5:
                lev = 2
            elif tl.index(task_id) == 8:
                lev = 3
            elif tl.index(task_id) == 11:
                lev = 4
            elif tl.index(task_id) == 14:
                lev = 5
            elif tl.index(task_id) == 17:
                lev = 6
        else:
            t = Task.objects.get(id=int(exp.LastTask))
            lev = t.Level
        stat = 0
        for t in Task.objects.filter(Level=lev, Task_user=exp):
            if t.Checking == "Решено":
                stat += 1
            else:
                stat = 0
        if stat != 3:
            li = []
            k = ''
            v = ''
            g = generator.generate_lv(lev)
            for key in g:
                k = key
                v = g[key]
            task_lv1 = Task(
                Task_user=exp,
                Level=lev,
                Quest=k,
                Answer=v
            )
            task_lv1.save(force_insert=True)
            id = task_lv1.id
            if not exp.Mistake:
                exp.LastTask = str(task_id)
            exp.Mistake = True
            if exp.MistakeList != None:
                li = exp.MistakeList.split(',')
                li.append(str(id))
                exp.MistakeList = ','.join(li)
            else:
                li.append(str(id))
                exp.MistakeList = ','.join(li)

            exp.save()
            return redirect('/tasks/task/%s' % li[len(li)-1])
        elif stat == 3:
            if exp.Mistake:
                exp.Mistake = False
                exp.save()
                tl = exp.TaskList.split(',')
                if tl.index(exp.LastTask) == len(tl)-1:
                    return redirect('/tasks/finalPage')
                return redirect('/tasks/task/%s' % tl[tl.index(exp.LastTask)+1])

    if tl.index(task_id) == len(tl)-1:
        return redirect('/tasks/finalPage')

    tl = exp.TaskList.split(',')

    if exp.Mistake:
        tl = exp.MistakeList.split(',')

    return redirect('/tasks/task/%s' % tl[tl.index(task_id)+1])


def task(request, task_id):
    variant_form = VariantForm
    args = {}
    args.update(csrf(request))
    args['task'] = Task.objects.get(id=task_id)
    args['form'] = variant_form
    t = Task.objects.get(id=task_id)
    t.StartTime = time.time()
    t.save()
    exp = Experiment.objects.get(Name=request.user)
    if exp.Info == 'Закрыто':
        return render_to_response('tasks/task_cl_1.html', args)
    args['variants'] = Variant.objects.filter(Variant_task=Task.objects.get(id=task_id))
    return render_to_response('tasks/task.html', args)


def addVariant(request, task_id):
    if request.POST:
        form = VariantForm(request.POST)
        if form.is_valid():
            t = Task.objects.get(id=task_id)
            var = form.save(commit=False)
            var.Variant_task = Task.objects.get(id=task_id)
            nums = str(var.Variant)
            try:
                s1 = int(nums[0]) + int(nums[1]) + int(nums[2])
                s2 = int(nums[3]) + int(nums[4]) + int(nums[5])
            except IndexError:
                args = {}
                args['error'] = 'Введите корректный номер билета (6 цифр)'
                args['task_id'] = "/tasks/" + str(task_id)
                return render_to_response("tasks/error.html", args)
            except ValueError:
                args = {}
                args['error'] = 'Введите номер следующего счастливого билета'
                args['task_id'] = "/tasks/" + str(task_id)
                return render_to_response("tasks/error.html", args)
            if s1 == s2 and var.Variant != Task.objects.get(id=task_id).Answer:
                var.Check = 'Счастливый, но не ближайший'
                t.Checking = 'Счастливый, но не ближайший'
            elif var.Variant == Task.objects.get(id=task_id).Answer:
                var.Check = 'Решено'
                t.Checking = 'Решено'
            else:
                var.Check = Variant.Check
            var.AnswerTime = time.time()

            # var.time = var.answerTime - t.StartTime
            delta = var.AnswerTime - t.StartTime
            var.Time = round(delta, 2)
            if t.Ans_number == 0:
                t.var_time1 = var.Time
            elif t.Ans_number == 1:
                t.var_time2 = var.Time
            elif t.Ans_number == 2:
                t.var_time3 = var.Time
            t.Ans_number += 1
            t.save()
            form.save()

        check = 0
        exp = Experiment.objects.get(Name=request.user)
        for task in Task.objects.filter(Task_user__Name=request.user):

            if exp.Info == "Открыто":
                if task.Checking == 'Решено':
                    check += 1
                else:
                    break
            else:
                if Variant.objects.filter(Variant_task=task).count() > 0:
                    check += 1
                else:
                    break
            if check == len(Task.objects.filter(Task_user__Name=request.user)):
                return redirect('/tasks/finalPage')
    strategy = exp.Strategy
    return redirect('/tasks/intro/%s/taskList' %strategy)


def final(request):
    check = 0
    for t in Task.objects.filter(Task_user__Name=request.user):
        if t.Checking == 'Решено':
            check += 1
    exp = Experiment.objects.get(Name=request.user)
    exp.EndTime = time.time()
    delta = exp.EndTime - exp.StartTime
    exp.Timing = round(delta, 2)
    exp.save()
    args = {}
    strategy = exp.Strategy
    if strategy == 7 or strategy == 8:
        args['time'] = exp.Timing
        return render_to_response('tasks/final.html', args)

    args['checks'] = str(check)
    return render_to_response('tasks/finalPage.html', args)


def taskList(request):
    args = {}
    exp = Experiment.objects.get(Name=request.user)
    strategy = exp.Strategy
    if strategy == 1:
        args['tasks'] = Task.objects.filter(Task_user__Name=request.user)
    elif strategy == 2:
        args['tasks'] = Task.objects.filter(Task_user__Name=request.user).order_by('-Level')
    elif strategy == 3:
        args['tasks'] = Task.objects.filter(Task_user__Name=request.user).order_by('?')
    args['strategy'] = strategy
    if exp.Info == 'Закрыто':

        return render_to_response('tasks/tasks_cl.html', args)
    return render_to_response('tasks/tasks.html', args)


def statistics(request):
    return render(request, 'tasks/statistics.html')

def statistic(request, strategy):
    args ={}
    args['experiment'] = Experiment.objects.filter(Strategy=strategy)
    args['strategy'] = strategy
    return render_to_response('tasks/statistic_list.html', args)

def experiment(request, experiment_id):
    exp = Experiment.objects.get(id=experiment_id)
    tasks = Task.objects.filter(Task_user=exp)
    count_g = 0 # посдсчет решенных
    count_b = 0 # подсчет не решенных
    count_nb = 0 # подсчет  счастливых но не ближайших
    full = 0
    times = []
    time_of_task = []
    time_of_task_avg = []
    diff_of_time = [0]
    if exp.Strategy in (1,2,3):
        i = 1
        for t in tasks:
            count = 0
            tm = 0.0
            for v in Variant.objects.filter(Variant_task = t):
                full += 1
                count += 1
                times.append(v.Time)
                tm += v.Time
                if v.Check == 'Решено':
                    count_g += 1
                elif v.Check == 'Счастливый, но не ближайший':
                    count_nb += 1
                else:
                    count_b += 1
            time_of_task.append(tm/count)
            if len(time_of_task) > 1:
                diff_of_time.append(abs(time_of_task[i]-time_of_task[i-1]))
                t.Diff = abs(time_of_task[i]-time_of_task[i-1])
                i += 1
            t.Time = tm
            t.save()
    elif exp.Strategy in (4,5,7,8):
        i = 1
        for t in tasks:
            count = 0
            tm = 0.0
            for v in Variant.objects.filter(Variant_task=t):
                full += 1
                count += 1
                times.append(v.Time)
                tm += v.Time
                if v.Check == 'Решено':
                    count_g += 1
                elif v.Check == 'Счастливый, но не ближайший':
                    count_nb += 1
                else:
                    count_b += 1
            if exp.Strategy == 7 and count != 0:
                time_of_task.append(tm/count)
                t.Time = tm/count
            elif exp.Strategy == 7 and count == 0:
                time_of_task.append(0.0)
            else:
                time_of_task.append(tm)
                t.Time = tm
            if len(time_of_task) > 1:
                diff_of_time.append(abs(time_of_task[i]-time_of_task[i-1]))
                t.Diff = abs(time_of_task[i] - time_of_task[i-1])
                i += 1

            t.save()
    Define_lev(t.id)
    g_pct = count_g/full * 100
    b_pct = count_b/full * 100
    nb_pct = count_nb/full * 100
    median_all = med(times)
    args = {}
    args['tasks'] = tasks
    args['experiment'] = Experiment.objects.get(id=experiment_id)
    args['g_pct'] = g_pct
    args['b_pct'] = b_pct
    args['nb_pct'] = nb_pct
    args['avg_task_time'] = avg(time_of_task)
    args['median_all'] = median_all #медиана времени ответа
    args['avg_of_diff'] = sum(diff_of_time)/(len(diff_of_time)-1)
    args['median_of_diff'] = med(diff_of_time)

    return render_to_response('tasks/experiment.html', args)

def variants(request, task_id):
    args = {}
    args['variants'] = Variant.objects.filter(Variant_task=Task.objects.get(id=task_id))
    args['task'] = Task.objects.get(id=task_id)
    return render_to_response('tasks/variants.html', args)

# Create your views here.

def Define_lev(task_id):
    t = Task.objects.get(id=task_id)
    q = t.Quest
    a = t.Answer
    s1q = int(q[0]) + int(q[1]) + int(q[2])
    s2q = int(q[3]) + int(q[4]) + int(q[5])
    s1a = int(a[0]) + int(a[1]) + int(a[2])
    s2a = int(a[3]) + int(a[4]) + int(a[5])
    if s1q < s2q and s2q > s2a and s1q > s1a:
        t.sub_lev = 1
    t.save


