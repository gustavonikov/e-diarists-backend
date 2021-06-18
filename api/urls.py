from .views import DiaristsCityList
from django.urls import path

urlpatterns = [
    path('diarists-by-city', DiaristsCityList.as_view(), name='diarists-by-city'),
]
