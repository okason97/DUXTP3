from django.urls import path

from . import views

urlpatterns = [
	path('pedirAyuda/', views.pedirAyuda, name='ask4Help'),
    path('text/', views.text, name='text'),
    path('', views.index, name='index'),
    path('disasterInfo/', views.disasterInfo, name='disasterInfo'),
]