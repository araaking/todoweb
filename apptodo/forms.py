from django import forms
from django.db.models import fields 
from django.forms import ModelForm
from .models import *

class formTodo(forms.ModelForm):
    
     class Meta:
        model = db_todo
        fields = '__all__'
         
        