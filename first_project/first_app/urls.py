from django.urls import path
from . import views

# views.index is a refernce to that funtion in views.py
urlpatterns = [
    path('', views.index, name='index'),
]
