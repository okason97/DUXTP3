from django.urls import path

from . import views

urlpatterns = [
	path('pedirAyuda/', views.pedirAyuda, name='pedirAyuda'),
    path('', views.index, name='index'),
]