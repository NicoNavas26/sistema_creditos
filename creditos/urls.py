from django.urls import path
from . import views

urlpatterns = [
    path('simulador/', views.simular_credito, name='simular_credito'),
]