from json.tool import main
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]