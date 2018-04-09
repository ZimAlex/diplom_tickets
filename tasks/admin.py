from django.contrib import admin
from .models import experiment, task_m, variant

admin.site.register(experiment)
admin.site.register(task_m)
admin.site.register(variant)
# Register your models here.
