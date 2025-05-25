# STRINGS
"""
Es una secuencia de caracteres encerrados entre comillas simples(') o dobles ("). Los strings son inmutables, lo que significa que una vez que se crean, no se pueden modificar. Los strigns son una parte fundamental de Python, y se utilizan para almacenar y manipular texto de cualquier tipo, como nombres, direcciones, mensajes, etc.
"""

# Strings con comillas simples
string_comillas_simples = "Este es un string con comillas simples"
print(string_comillas_simples)

# Strings con comillas dobles
string_comillas_dobles = "Este es un string con comillas dobles"
print(string_comillas_dobles)

# Strings con comillas triples simples
string_comillas_triples_simples = (
    """Este string con comillas simples puede ser multi-línea"""
)
print(string_comillas_triples_simples)

# Strings con comillas triples dobles
string_comillas_triples_dobles = (
    """Este string con comillas dobles puede ser multi-línea"""
)
print(string_comillas_triples_dobles)

# -------------------------------
texto = "hOlA mUndO"
texto_con_espacios = "        texto con espacios        "
texto_separado = "Pytho,JavaScript,Django,React"
lista = ["Hola", "Juan", "Carlos"]
numeros = "123456"
repeticion = "manzana, naranja, manzaza, naranja"

print(texto)
print(
    "capitalize:", texto.capitalize()
)  # Convierte la primera letra en mayúscula (el resto en minúscula)
print("upper:", texto.upper())  # Convierte el texto entero en mayúsculas
print("lower:", texto.lower())  # Convierte el texto entero en minúsculas
print(
    "strip:", texto_con_espacios.strip()
)  # Elimina los espacios al comienzo y al final
print(
    "replace:", texto_con_espacios.replace("espacios", "gracias")
)  # Reemplaza una palabra por otra
print("split:", texto_separado.split(","))  # Separa texto en items de una lista
print("join:", ",".join(lista))  # Junta los items de una lista en un string
print(
    "find:", texto.find("mUndO")
)  # Muestra la posición donde arranca el texto ingresado
print(
    "startswith:", texto.startswith("Adios")
)  # Indica si comienza o no con la palabra ingresada
print(
    "endswith:", texto.endswith("Adios")
)  # Indica si finaliza o no con la palabra ingresada
print(
    "isdigit:", numeros.isdigit()
)  # Indica si todos los caracteres son números (espacios no cuentan)
print(
    "isalpha:", texto.isalpha()
)  # Indica si todos los caracteres son letras (espacios no cuentan)
print(
    "isalnum:", texto.isalnum()
)  # Indica si todos los caracteres son alfanuméricos o no (espacios no cuentan)
print(
    "isspace:", texto.isspace()
)  # Indica si el string no contiene caracteres (solo hecho de espacios)
print(
    "count:", repeticion.count("manzana")
)  # Indica cuántas veces se repite la palabra ingresada
print(
    "index:", texto.index("m")
)  # Indica cuál es la primera posición o indice en la que encuentra la palabra ingresada

# -------------------------------

# CADENA DE CARACTERES

# ------------STRINGS------------

string_comillas_simples = "Hola Mundo"

string_comillas_dobles = "Hola Mundo"

string_comillas_triples_simples = """Este texto puede ser multi-línea"""

string_comillas_triples_dobles = """También se pueden utilizar múltiples líneas"""

# -------------------------------

txt = "Seguimos trabajando con strings"  # se cuenta caracter desde el 0

# Slicing: ponemos desde un índice hasta un índice NO incluido

# "S e g u i m o s   t r  a  b  a  j  a  n  d  o     c  o  n     s  t  r  i  n  g  s"
# "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30"

# para traernos la palabra trabajando hay que seleccionar del caracter 8 al 19, ya que el 18 excluye la última letra de la palabra

# print(txt[8:18]) # no incluye el caracter 18 - ' trabajand'

# print(txt[8:19]) # incluye el caracter 18 - ' trabajando'

# print(txt[:8]) # desde el comienzo hasta el caracter 8 - 'Seguimos'

# print(txt[23:]) # desde el caracter 23 hasta el final - ' strings'

# print(txt[-7:]) # me paro en la posición 7 desde la derecha y ahí cuento hasta el final - 'strings'

# print(txt[-7:-1]) # me paro en la posición 7 desde la derecha y ahí cuento hasta el anteúltimo caracter - 'string'

# print(txt[-11:-1]) # me paro en la posición 11 desde la derecha y ahí cuento hasta el anteúltimo caracter - 'con string'

# -------------------------------

txt = "CUANDO ESCRIBO EN MAYUSCULA TODOS PIENSAN QUE ESTOY GRITANDO"

minusculas = txt.lower()  # transformo la cadena de caracteres en lowercase

# print(minusculas)

# -------------------------------

txt_dos = "este texto es tan importante que si lo pongo en minúsculas nadie le presta atención"

mayusculas = txt_dos.upper()  # transformo la cadena de caracteres en uppercase

# print(mayusculas)

# -------------------------------

# STRIP

txt_tres = "         quedaron espacios al comienzo y al final    "

# print(txt_tres)

txt_cuatro = "clave "

# print(txt_cuatro)

txt_tres_strip = txt_tres.strip()

# print(txt_tres_strip)

txt_cuatro_strip = txt_cuatro.strip()

# print(txt_cuatro_strip)

# -------------------------------

a = "Hola"
b = "Mundo"
c = a + " " + b  # concatenar
# print(c)

txt = "El contenido de este curso va a durar: "
horas = 10

# concatenado = txt + horas + " horas"  # error txt=str + horas=int
# print(concatenado)

horas = 10
txt = "El contenido de este curso va a durar: {} horas"  # como si fuera un parámetro

concatenado = txt.format(horas)
# print(concatenado)

horas = 10
clases = 60
txt = "El contenido de este curso va a durar: {} horas y tendrá {} clases"  # como si fuera un parámetro

concatenado = txt.format(horas, clases)
# print(concatenado)

horas = 10
clases = 60
txt = "El contenido de este curso va a durar: {1} horas y tendrá {0} clases"  # le pongo orden específico en el que van a ser ingresados los valores

concatenado = txt.format(clases, horas)
# print(concatenado)

# -------------------------------

# CARACTERES NO PERMITIDOS

# Si a un texto le tengo que poner comillas dobles o simples (funciona igual)

# con la barra invertida(\) -> escape de caracteres

# \ -> alt+92
# \n -> salto de línea
# \b -> backspace

txt = 'La mejor serie que vi en mi vida es "Friends"'

# print(txt)

# excapar barra de escape (en caso de que el string contenga la barra de escape a proposito - ruta de un archivo)

txt = "La carpeta donde tengo este curso es c:\\Users\\virpi\\Desktop\\Titi\\DIGITAL HOUSE\\Python 2024\\VSCODE"

# print(txt)

# -------------------------------

# VER IMAGEN CON FUNCIONES: Archivo descargable_ string methods.png
