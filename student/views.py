from django.shortcuts import render
from .models import StudentList

def List(request):
    std = StudentList.objects.all()
    context = {
        'student' : std
    }
    return render(request, 'student-list.html', context)

def Detail(request, roll):
    student = StudentList.objects.get(id=roll)
    context = {
        'std' : student
    }
    return render(request, 'student-detail.html', context)    