from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('countwords/', views.count, name='counts'),
    path('about/', views.about, name='abouts'),
    ]
