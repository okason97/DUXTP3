from django.urls import path

from . import views

urlpatterns = [
	path('pedirAyuda/', views.pedirAyuda, name='pedirAyuda'),
    path('text/', views.text, name='text'),
    path('', views.index, name='index'),
]