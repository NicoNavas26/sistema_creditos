from django.contrib import admin
from .models import Cliente, Prestamo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('documento', 'nombres', 'apellidos', 'telefono', 'creado_at')
    search_fields = ('documento', 'nombres', 'apellidos')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'monto', 'tasa_interes', 'plazo_meses', 'estado')
    list_filter = ('estado', 'fecha_inicio')
    search_fields = ('cliente__documento', 'cliente__nombres')