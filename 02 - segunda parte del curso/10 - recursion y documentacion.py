# RECURSION
# llamar a una función dentro de si misma


def suma_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_naturales(n - 1)


# print(suma_naturales(5)) # devuelve 15 -> 5+4+3+2+1


def factoriales(n):
    if n == 0:
        return 1
    else:
        return n * factoriales(n - 1)


# print(factoriales(5))  # devuelve 120 -> 5*4*3*2*1*1 (2 veces '*1' porque cuando es 0 devuelve 1)


# Parecido a un bucle
def contador(n):  # pasamos argumento
    print(n)  # imprimimos ese argumento
    n += 1  # le sumamos 1
    if n <= 10:  # mientras esta condicion no se cumpla
        contador(
            n
        )  # vuelve a llamar a la funcion que va a seguir sumando hasta llegar al 10


# contador(1)

# -------------------------------
"""-------------------"""
# -------------------------------

# DOCUMENTACION


def suma(a, b):
    # cuando hacemos """ y le damos a enter con la función ya armada va a armar la estructura mínima para el docstring
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a + b


def suma_dos(a, b):
    # cuando hacemos """ y le damos a enter con la función ya armada va a armar la estructura mínima para el docstring
    """
    Esta función suma dos números y devuelve el resultado

    Args:
        a (int): El primer número a sumar
        b (int): El segundo número a sumar

    Returns:
        int: La suma de los dos números.
    """
    return a + b


print(suma_dos.__doc__)  # devuelve
#### Esta función suma dos números y devuelve el resultado
####
#### Args:
####     a (int): El primer número a sumar
####     b (int): El segundo número a sumar
####
#### Returns:
####     int: La suma de los dos números.

help(suma_dos)  # devuelve
####Help on function suma_dos in module __main__:
####
####suma_dos(a, b)
####    Esta función suma dos números y devuelve el resultado
####
####    Args:
####        a (int): El primer número a sumar
####        b (int): El segundo número a sumar
####
####    Returns:
####        int: La suma de los dos números.
