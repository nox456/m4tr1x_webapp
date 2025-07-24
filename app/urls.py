from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('grafica-3d/', views.grafica3D, name='grafica_3d'),
]