from django.shortcuts import render_to_response, redirect, render


from .models import Experiment, Task, Variant
from . import generator
from .forms import VariantForm
from django.template.context_processors import csrf
import time
import random


def generate(request):
    r = random.randint(1,7)
    r = 8
    c = random.randint(0,1)
    c = 1
    if c == 1:
        inf = 'Открыто'
    else:
        inf = 'Закрыто'
    # r = 7
    if r == 7:
        repl = True
    else:
        repl = False
    exp = Experiment(
        replay=repl,
        info=inf,
        strategy=r,
        mistake=False,
        name=request.user
    )
    exp.save(force_insert=True)
    g = generator.generate()
    for lev in range(0, len(g)):
        for key in (g[lev]):
            t = Task(
                task_user=exp,
                level=lev+1,
                quest=key,
                answer=g[lev][key],
            )
            t.save(force_insert=True)
    args = {}

    return redirect('/tasks/intro')


def main(request):
    exp = Experiment.objects.get(name = request.user)
    exp.startTime = time.clock()
    exp.save()
    args = {}
    args['strategy'] = exp.strategy
    return render_to_response('tasks/mainPage.html', args)


def createList(request):
    l = []
    exp = Experiment.objects.get(name=request.user)
    strategy = exp.strategy
    for t in Task.objects.filter(task_user__name=request.user):
        l.append(str(t.id))
    if strategy == 5:
        l = l.reverse()
    elif strategy == 6:
        l = random.shuffle(l)
    exp = Experiment.objects.get(name=request.user)
    exp.taskList = ','.join(l)
    exp.save(force_insert=False)
    return redirect('/tasks/task/%s' % l[0])


def getTask(request, task_id):

    variant_form = VariantForm
    exp = Experiment.objects.get(name=request.user)
    if exp.mistake:
        tl = exp.mistakeList.split(',')
    else:
        tl = exp.taskList.split(',')
    ml = []


    if  exp.strategy != 8 and tl.index(task_id) == len(tl)-1:
        if exp.replay and not exp.mistake:
            for id in tl:
                task = Task.objects.get(id=id)
                if task.checking != 'Решено' and task.checiking != 'Счастливый, но не ближайший':
                    ml.append(id)
            exp.mistakeList = ','.join(ml)
            exp.mistake = True
            exp.save()
            return redirect('/tasks/mistakes/%s' % ml[0])
        else:
            return redirect('/tasks/finalPage')
    args = {}
    args.update(csrf(request))
    args['task'] = Task.objects.get(id=task_id)
    args['form'] = variant_form
    t = Task.objects.get(id=task_id)
    t.startTime = time.clock()
    t.save()
    if exp.info == "Открыто":
        if not exp.mistake and str(int(task_id)-1) in exp.taskList:
            t2 = Task.objects.get(id=str(int(task_id)-1))
            args['check'] = t2.checking
        elif exp.mistake and str(int(task_id)-1) in exp.mistakeList:
            t2 = Task.objects.get(id=str(int(task_id) - 1))
            args['check'] = t2.checking
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
            if not isint(var.variant) or len(var.variant) != 6:
                return redirect('/tasks/task/%s' % task_id)
            var.variant_task = Task.objects.get(id=task_id)
            nums = str(var.variant)
            s1 = int(nums[0]) + int(nums[1]) + int(nums[2])
            s2 = int(nums[3]) + int(nums[4]) + int(nums[5])


            if s1 == s2 and var.variant != Task.objects.get(id=task_id).answer:
                var.check = 'Счастливый, но не ближайший'
                t.checking = 'Счастливый, но не ближайший'
            elif var.variant == Task.objects.get(id=task_id).answer:
                var.check = 'Решено'
                t.checking = 'Решено'
            else:
                var.check = Variant.check
            var.answerTime = time.clock()
            # var.time = var.answerTime - t.startTime
            var.time = float('{:.3f}'.format(var.answerTime - t.startTime))
            t.save()
            form.save()
    exp = Experiment.objects.get(name=request.user)
    tl = exp.taskList.split(',')
    if exp.mistake:
        check = True
    else:
        check = tl.index(task_id) == 2 or tl.index(task_id) == 5 or tl.index(task_id) == 8 or tl.index(task_id) == 11 or tl.index(task_id) == 14 or tl.index(task_id) == 17
    if exp.strategy == 8 and check:

        if not exp.mistake:

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
            t = Task.objects.get(id=int(exp.lastTask))
            lev = t.level
        stat = 0
        for t in Task.objects.filter(level=lev, task_user=exp):
            if t.checking == "Решено":
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
                task_user=exp,
                level=lev,
                quest=k,
                answer=v
            )
            task_lv1.save(force_insert=True)
            id = task_lv1.id
            if not exp.mistake:
                exp.lastTask = str(task_id)
            exp.mistake = True
            if exp.mistakeList != '':
                li = exp.mistakeList.split(',')
                li.append(str(id))
                exp.mistakeList = ','.join(li)
            else:
                li.append(str(id))
                exp.mistakeList = ','.join(li)

            exp.save()
            return redirect('/tasks/task/%s' % li[len(li)-1])
        elif stat == 3:
            if exp.mistake:
                exp.mistake = False
                exp.save()
                tl = exp.taskList.split(',')
                if tl.index(exp.lastTask) == len(tl)-1:
                    return redirect('/tasks/finalPage')
                return redirect('/tasks/task/%s' % tl[tl.index(exp.lastTask)+1])
            else:
                if tl.index(task_id) == len(tl)-1:
                    return redirect('/tasks/finalPage')


    tl = exp.taskList.split(',')

    if exp.mistake:
        tl = exp.mistakeList.split(',')

    return redirect('/tasks/task/%s' % tl[tl.index(task_id)+1])


def task(request, task_id):
    variant_form = VariantForm
    args = {}
    args.update(csrf(request))
    args['task'] = Task.objects.get(id=task_id)
    args['form'] = variant_form
    t = Task.objects.get(id=task_id)
    t.startTime = time.clock()
    t.save()
    exp = Experiment.objects.get(name=request.user)
    if exp.info == 'Закрыто':
        return render_to_response('tasks/task_cl_1.html', args)
    args['variants'] = Variant.objects.filter(variant_task=Task.objects.get(id=task_id))
    return render_to_response('tasks/task.html', args)


def addVariant(request, task_id):
    if request.POST:
        form = VariantForm(request.POST)
        if form.is_valid():
            t = Task.objects.get(id=task_id)
            var = form.save(commit=False)
            var.variant_task = Task.objects.get(id=task_id)
            nums = str(var.variant)
            s1 = int(nums[0]) + int(nums[1]) + int(nums[2])
            s2 = int(nums[3]) + int(nums[4]) + int(nums[5])
            if s1 == s2 and var.variant != Task.objects.get(id=task_id).answer:
                var.check = 'Счастливый, но не ближайший'
                t.checking = 'Счастливый, но не ближайший'
            elif var.variant == Task.objects.get(id=task_id).answer:
                var.check = 'Решено'
                t.checking = 'Решено'
            else:
                var.check = Variant.check
            var.answerTime = time.clock()
            # var.time = var.answerTime - t.startTime
            var.time = float('{:.3f}'.format(var.answerTime - t.startTime))
            t.save()
            form.save()

        check = 0
        for task in Task.objects.filter(task_user__name = request.user):
            if task.checking == 'Решено':
                check += 1
            else:
                break
            if check == len(Task.objects.filter(task_user__name = request.user)):
                return redirect('/tasks/finalPage')
    exp = Experiment.objects.get(name=request.user)
    strategy = exp.strategy
    return redirect('/tasks/intro/%s/taskList' %strategy)


def final(request):
    check = 0
    for t in Task.objects.filter(task_user__name=request.user):
        if t.checking == 'Решено':
            check += 1
    exp = Experiment.objects.get(name=request.user)
    exp.Time = float('{:.3f}'.format(time.clock() - exp.startTime))
    exp.save()
    args = {}
    if exp.strategy == 7 or exp.strategy == 8:
        args['time'] = exp.Time
        return render_to_response('tasks/final.html', args)

    args['checks'] = str(check)
    return render_to_response('tasks/finalPage.html', args)


def taskList(request):
    args = {}
    exp = Experiment.objects.get(name=request.user)
    strategy = exp.strategy
    if strategy == 1:
        args['tasks'] = Task.objects.filter(task_user__name=request.user)
    elif strategy == 2:
        args['tasks'] = Task.objects.filter(task_user__name=request.user).order_by('-level')
    elif strategy == 3:
        args['tasks'] = Task.objects.filter(task_user__name=request.user).order_by('?')
    args['strategy'] = strategy
    if exp.info == 'Закрыто':
        return render_to_response('tasks/tasks_cl.html', args)
    return render_to_response('tasks/tasks.html', args)


def statistics(request):
    return render(request, 'tasks/statistics.html')

def statistic(request, strategy):
    args ={}
    args['experiment'] = Experiment.objects.filter(strategy=strategy)
    args['strategy'] = strategy
    return render_to_response('tasks/statistic_list.html', args)

def experiment(request, experiment_id):
    args = {}
    args['tasks'] = Task.objects.filter(task_user=Experiment.objects.get(id=experiment_id))
    return render_to_response('tasks/experiment.html', args)

def variants(request, task_id):
    args = {}
    args['variants'] = Variant.objects.filter(variant_task=Task.objects.get(id=task_id))
    args['task'] = Task.objects.get(id=task_id)
    return render_to_response('tasks/variants.html', args)

# Create your views here.
