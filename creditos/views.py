from django.shortcuts import render
from .utils import calcular_tabla_amortizacion

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