
from django.urls import path
from . import views

urlpatterns = [
    path('', views.metrika, name='metrika'),
   

]