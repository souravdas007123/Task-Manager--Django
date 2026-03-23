from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id','start_date','title','category','assigned','prioritize','end_date','status']