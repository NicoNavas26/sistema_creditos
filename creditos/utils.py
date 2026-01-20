from decimal import Decimal

def calcular_tabla_amortizacion(monto, tasa_interes, plazo):
    """
    Calcula la tabla de amortización usando el sistema de cuota fija (Francés).
    """
    # 1. Convertimos a Decimal para precisión financiera exacta
    monto = Decimal(monto)
    tasa = Decimal(tasa_interes) / 100  # Convertir 5% a 0.05
    plazo = int(plazo)

    # 2. Fórmula de Cuota Fija (Matemática Financiera)
    # R = P * [i * (1+i)^n] / [(1+i)^n - 1]
    if tasa > 0:
        cuota = monto * (tasa * (1 + tasa) ** plazo) / ((1 + tasa) ** plazo - 1)
    else:
        cuota = monto / plazo  # Si la tasa es 0%

    saldo = monto
    tabla = []

    # 3. Generamos el plan mes a mes
    for mes in range(1, plazo + 1):
        interes_mes = saldo * tasa
        capital_mes = cuota - interes_mes
        saldo -= capital_mes

        # Guardamos los datos del mes (redondeando a 2 decimales)
        tabla.append({
            "mes": mes,
            "cuota": round(cuota, 2),
            "interes": round(interes_mes, 2),
            "capital": round(capital_mes, 2),
            "saldo": round(max(0, saldo), 2)
        })

    return tabla