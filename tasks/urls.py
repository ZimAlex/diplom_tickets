from django.conf.urls import url
from . import views

# from .views import TaskList

urlpatterns = [
    url(r'generate/$', views.generate),
    url(r'^intro/$', views.main),
    url(r'^intro/1/taskList/$', views.taskList),
    url(r'^intro/2/taskList/$', views.taskList),
    url(r'^intro/3/taskList/$', views.taskList),
    url(r'^intro/4/taskList/$', views.createList),
    url(r'^intro/5/taskList/$', views.createList),
    url(r'^intro/6/taskList/$', views.createList),
    url(r'^intro/7/taskList/$', views.createList),
    url(r'^intro/8/taskList/$', views.createList),
    url(r'^task/(?P<task_id>\d+)$', views.getTask),
    url(r'^mistakes/(?P<task_id>\d+)$', views.getTask),
    url(r'^(?P<task_id>\d+)$', views.task),
    url(r'^task/variant/(?P<task_id>\d+)', views.addVariant_cl),
    url(r'^mistakes/variant/(?P<task_id>\d+)', views.addVariant_cl),
    url(r'^addvariant/(?P<task_id>\d+)$', views.addVariant),
    url(r'^finalPage/$', views.final),
    url(r'^statistic/$', views.statistics),
    url(r'^statistic/(?P<strategy>\d+)/$', views.statistic),
    url(r'experiment/(?P<experiment_id>\d+)$', views.experiment),
    url(r'experiment/(?P<task_id>\d+)/var/$', views.variants)

]