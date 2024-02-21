from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request,'index.html',{})


def table(request):
    return render(request,'table.html',{})
