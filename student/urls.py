from django.urls import path
from .views import List, Detail

urlpatterns = [
    path('/list', List, name='student-list'),
    path('/detail/<int:roll>', Detail, name='student-detail')
]