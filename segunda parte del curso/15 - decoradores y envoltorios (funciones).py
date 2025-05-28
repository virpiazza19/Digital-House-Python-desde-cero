# DECORADORES y ENVOLTORIOS (funciones)

# DECORATOR y WRAPPER


def decorador(funcion):
    def envoltorio():
        print(
            "Está funcionalidad se dispararía antes de la función que nos pasen por parámetro"
        )
        funcion()
        print(
            "Está funcionalidad se dispararía después de la función que nos pasen por parámetro"
        )

    return envoltorio


def saludar():
    print("Hola, estoy saludando")


saludo_decorado = decorador(
    saludar
)  # No escribo saludar() porque no quiero que se ejecute en el momento, sino cuando la llamo dentro del envoltorio

saludo_decorado()