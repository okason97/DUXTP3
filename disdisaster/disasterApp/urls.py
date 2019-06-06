from django.urls import path

from . import views

urlpatterns = [
	path('pedirAyuda/', views.ask4Help, name='ask4Help'),
    path('', views.index, name='index'),
    path('disasterInfo/', views.disasterInfo, name='disasterInfo'),
]