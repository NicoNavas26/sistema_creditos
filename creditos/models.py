from django.db import models
from django.db.models import Sum

class Cliente(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    creado_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.documento})"

class Prestamo(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente de Aprobación'),
        ('ACTIVO', 'Activo'),
        ('PAGADO', 'Pagado'),
        ('MORA', 'En Mora'),
        ('RECHAZADO', 'Rechazado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='prestamos')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2, help_text="Tasa mensual en %")
    plazo_meses = models.IntegerField()
    fecha_inicio = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    creado_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Préstamo {self.id} - {self.cliente.nombres} - ${self.monto}"
    def total_pagado(self):
        # Busca todos los pagos y suma la columna 'monto'
        resultado = self.pagos.aggregate(Sum('monto'))
        return resultado['monto__sum'] or 0

    def saldo_pendiente(self):
        # Resta simple: Lo que presté MENOS lo que me han devuelto
        return self.monto - self.total_pagado()
    
class Pago(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateField()
    nota = models.CharField(max_length=200, blank=True, null=True, help_text="Ej: Transferencia Bancolombia")
    creado_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Abono ${self.monto} - {self.prestamo}"