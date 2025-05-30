# ENCAPSULAMIENTO: ocultar los detalles internos (propiedades) de una clase y restringir el acceso directo a los atributos y métodos de la misma

from clases.cuenta_bancaria import CuentaBancaria

# Objeto/Instancia de CuentaBancaria

cuenta = CuentaBancaria("Virgina", 1000)

"""-----------------------------------------------"""

# print(cuenta.__saldo) # AttributeError: 'CuentaBancaria' object has no attribute '__saldo'. Did you mean: 'get_saldo'?

# print(cuenta.__titular) # AttributeError: 'CuentaBancaria' object has no attribute '__titular'

"""-----------------------------------------------"""

# Intento de modificación de titular y saldo

## cuenta.__titular = "Pepe"  # No se puede modificar directamente
## cuenta.__saldo = 10000000  # No se puede modificar directamente

## print(cuenta.get_saldo())  # Devuelve 1000

"""-----------------------------------------------"""

# Obtener saldo inicial
print(cuenta.get_saldo())

# Depositar 5000$
cuenta.depositar(5000)

# Obetener saldo actualizado
print(cuenta.get_saldo())

# Retirar 6001$
cuenta.retirar(6001)

# Retirar 600$
cuenta.retirar(600)
