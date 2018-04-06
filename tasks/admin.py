from django.contrib import admin
from .models import Experiment, Task, Variant

admin.site.register(Experiment)
admin.site.register(Task)
admin.site.register(Variant)
# Register your models here.
