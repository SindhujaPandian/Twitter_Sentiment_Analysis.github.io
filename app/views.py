from django.shortcuts import render
from app.forms import userForm
from app.sentiment import mlmodel
# Create your views here.
def home(request):
    return render(request,'app/home.html',{})

def index(request):
    form = userForm()
    return render(request,'app/index.html',{'form':form})

def result(request):
    res_dict={'result':'NEGATIVE'}
    return render(request,'app/result.html',res_dict)

def accuracy(request):
    return render(request,'app/accuracy.html',{})

def code(request):
    return render(request,'app/code.html',{})
