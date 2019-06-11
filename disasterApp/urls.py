from django.urls import path

from . import views

urlpatterns = [
	path('pedirAyuda/', views.ask4Help, name='ask4Help'),
    path('info/<str:disasterName>', views.text, name='text'),
    path('', views.index, name='index'),
]