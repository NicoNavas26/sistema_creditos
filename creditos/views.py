from django.shortcuts import render, redirect, get_object_or_404
from .utils import calcular_tabla_amortizacion
from .models import Prestamo
from .forms import PrestamoForm

def simular_credito(request):
    tabla = []
    error = None

    # 1. Detectar si el usuario envió el formulario (POST)
    if request.method == 'POST':
        try:
            # 2. Capturar los datos enviados desde el navegador
            monto = request.POST.get('monto')
            tasa = request.POST.get('tasa')
            plazo = request.POST.get('plazo')

            # 3. Llamar a nuestra función matemática (que creamos en el paso anterior)
            # Nota: Los datos llegan como texto, la función utils se encarga de convertirlos.
            tabla = calcular_tabla_amortizacion(monto, tasa, plazo)
            
        except ValueError:
            error = "Por favor ingrese números válidos."

    # 4. Renderizar: Enviar los datos resultantes a la plantilla HTML
    return render(request, 'creditos/simulador.html', {
        'tabla': tabla,
        'error': error
    })

def crear_prestamo(request):
    if request.method == 'POST':
        # Procesar datos enviados
        form = PrestamoForm(request.POST)
        if form.is_valid():
            nuevo_prestamo = form.save()
            # Redirigir al detalle (crearemos esta ruta en pasos siguientes)
            return redirect('detalle_prestamo', prestamo_id=nuevo_prestamo.id)
    else:
        # Mostrar formulario vacío
        form = PrestamoForm()

    return render(request, 'creditos/crear_prestamo.html', {'form': form})

def detalle_prestamo(request, prestamo_id):
    # 1. Buscar el préstamo por su ID. Si no existe, muestra error 404.
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)

    # 2. Recalcular la tabla de pagos para visualizarla
    tabla = calcular_tabla_amortizacion(
        prestamo.monto, 
        prestamo.tasa_interes, 
        prestamo.plazo_meses
    )

    # 3. Enviar datos a la plantilla
    return render(request, 'creditos/detalle_prestamo.html', {
        'prestamo': prestamo,
        'tabla': tabla
    })

def listar_prestamos(request):
    # Traemos TODOS los préstamos de la base de datos
    # order_by('-creado_at') hace que salgan los más nuevos primero
    prestamos = Prestamo.objects.all().order_by('-creado_at')
    
    return render(request, 'creditos/lista_prestamos.html', {
        'prestamos': prestamos
    })