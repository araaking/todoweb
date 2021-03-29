from django.contrib import admin
from .models import db_todo

# Register your models here.
class db_todolist(admin.ModelAdmin):
    list_display = ['namaPekerjaan','startdate','status']
    
admin.site.register(db_todo,db_todolist)