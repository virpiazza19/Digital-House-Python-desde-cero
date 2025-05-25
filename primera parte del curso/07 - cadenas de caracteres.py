# CADENA DE CARACTERES

# ------------STRINGS------------

string_comillas_simples = 'Hola Mundo'

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

txt = "La mejor serie que vi en mi vida es \"Friends\""

#print(txt)

# excapar barra de escape (en caso de que el string contenga la barra de escape a proposito - ruta de un archivo)

txt = "La carpeta donde tengo este curso es c:\\Users\\virpi\\Desktop\\Titi\\DIGITAL HOUSE\\Python 2024\\VSCODE"

#print(txt)

#-------------------------------

#VER IMAGEN CON FUNCIONES: Archivo descargable_ string methods.png

