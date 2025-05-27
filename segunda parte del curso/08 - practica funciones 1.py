# # Función sin parámetros
# def saludar():
#     print("Hola mundo!")
#
# saludar()

## # Función con un parámetro
## def saludar(nombre):
##     print(f"Hola {nombre}!")
##
## saludar("Vir")

### # Función que pide dos parámetros pero recibe un solo argumento
### def saludar(nombre, apellido):
###     print(f"Hola {nombre}!")
###
### saludar("Vir") # TypeError: saludar() missing 1 required positional argument: 'apellido'

### def saludar(nombre, apellido): # el color de 'apellido' está más opaco porque el parámetro no se está usando
###     print(f"Hola {nombre}!")
###
### saludar("Vir","Piazza") # Por más de que en la función no se utilize el parámetro, mientras no tenga un valor predefinido, es requerido pasarlo cuando llamamos a la función

# Función X cantidad de parámetros -> cuando no sé cuántos parámetros se van a enviar
def saludar(*nombres):
    for nombre in nombres:
        print(f"Hola {nombre}!")


## saludar("Vir", "Pedro")


### def saludos(*nombres):
###     if len(nombres) == 2:
###         print(f"Hola {nombres[0]}, {nombres[1]}!")
###     elif len(nombres) > 2:
###         for nombre in nombres:
###             print(f"Hola {nombre}!")
###     else:
###         print(f"Hola {nombres[0]}!")
### 
### 
### saludos("Juan")
### saludos("Juan", "Pedro")
### saludos("Juan", "Pedro", "Maria")

def padre_orgulloso(hija1,hija2,hija3):
    print("Mis hijas son",hija1,",",hija2,"y",hija3)
    print("Y la más pequeña es", hija3)

padre_orgulloso("Bombon","Burbuja","Bellota")

# KEY WORD ARGUMENTS -> asignar los argumentos a los parámetros sin necesariamente seguir el orden estipulado

padre_orgulloso(hija1="Bombon",hija3="Burbuja",hija2="Bellota")
