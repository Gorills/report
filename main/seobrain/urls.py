
from django.urls import path
from . import views

urlpatterns = [
    path('', views.seo, name='seo'),
    path('<int:pk>/', views.seo_update, name='seo_update'),
   

]