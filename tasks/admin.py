from django.contrib import admin
from tasks.models import Task
class Taskadmin(admin.ModelAdmin):
    list_display=['id','title','description','status','priority','due_date','created_at','updated_at','user']
admin.site.register(Task,Taskadmin)