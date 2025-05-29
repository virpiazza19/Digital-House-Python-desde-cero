tipo_cambio_eur_a_mxn = 23.70
tipo_cambio_usd_a_mxn = 20.75

tipo_conversion = input("Ingrese la moneda origen para la conversión (EUR/USD):").upper()
monto = float(input("Ingrese el monto a convertir: "))

if tipo_conversion == "EUR":
    resultado = monto * tipo_cambio_eur_a_mxn
    print("El resultado de la conversión", tipo_conversion, "a MXN es", resultado)
elif tipo_conversion == "USD":
    resultado = monto * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión", tipo_conversion, "a MXN es", resultado)
else:
    print("Tipo de conversión no válido")