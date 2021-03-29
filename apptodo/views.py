from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import db_todo
from .forms import formTodo
# Create your views here.
def home(request):
    dbtodo = db_todo.objects.all()
    context = {'dbtodo':dbtodo}
    return render(request,'index.html', name='home')

def create(request):
    dbtodo = db_todo.objects.all()
    forms = formTodo()
    
    if request.method == 'POST':
        forms = formTodo()
        if forms.is_valid():
            forms.save()
            return redirect('/')
    context = {'dbtodo':dbtodo, 'forms':forms}
    return render(request,'create.html',name='create')

def update(request,pk):
    dbtodo = db_todo.objects.get(id=pk)
    forms = formTodo(request.POST or None, instance=dbtodo)
    
    if forms.is_valid():
        forms.save
        return redirect('/'+ pk)
    
    context = {'dbtodo':dbtodo, 'forms':forms}
    return render(request,'update.html',name='update')

def delete(request,pk):
    item_delete = db_todo.objects.get(id=pk)
    if request.method == 'POST':
        db_todo.delete()
        return redirect('/')
    
    
    context = {
        'todo': item_delete
               }
    
    return render(request,'delete.html',context)