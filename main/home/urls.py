
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('img_remove/<int:pk>/', views.img_remove, name='img_remove'),


    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('report/edit/<int:pk>/', views.report_edit, name='report_edit'),

    path('<slug:parent>/<int:pk>/', views.report_detail, name='report_detail'),
   

]