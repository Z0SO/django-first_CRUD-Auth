from django.contrib import admin
from .models import Task

# Register your models here.


class Task_Admin(admin.ModelAdmin):
    readonly_fields = (
        'fecha_creacion',

    )


admin.site.register(Task, Task_Admin)
