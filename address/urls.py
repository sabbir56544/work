from django.urls import path
from .views import Area_List, Area_Detail

urlpatterns = [
    path('/list' ,Area_List, name='address-list'),
    path('/detail/<int:area_no>', Area_Detail, name='address-detail')
]

