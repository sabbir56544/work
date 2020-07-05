from django.http import HttpResponse
from django.shortcuts import render

def Home(requset):
    return render(requset, 'home.html')

def About(requset):
    return render(requset, 'about.html')

def Register(requset):
    return render(requset, 'register.html')