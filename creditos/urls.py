from django.urls import path
from . import views

urlpatterns = [
    # ESTA SERÁ TU PÁGINA DE INICIO (Ruta vacía '')
    path('', views.listar_prestamos, name='listar_prestamos'),
    # Ruta del simulador (la que ya tenías)
    path('simulador/', views.simular_credito, name='simular_credito'),
    
    # NUEVA: Ruta para el formulario de registro
    path('crear-prestamo/', views.crear_prestamo, name='crear_prestamo'),
    
    # NUEVA: Ruta dinámica (el número cambia según el préstamo)
    path('prestamo/<int:prestamo_id>/', views.detalle_prestamo, name='detalle_prestamo'),
]