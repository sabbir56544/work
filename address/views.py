from django.shortcuts import render
from django.http import HttpResponse
from .models import AreaList

def Area_List(request):
    area_list = AreaList.objects.all()
    context = {
        'area' : area_list
    }
    return render(request, 'address-list.html', context)

def Area_Detail(request, area_no):
    area_detail = AreaList.objects.get(area_no=area_no)
    context = {
        'areas' : area_detail
    }
    return render(request, 'address-detail.html', context)
