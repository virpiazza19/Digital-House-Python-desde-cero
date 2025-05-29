# FOR

for i in range(5): # de la posición 0 a 4
    print(i)

#-------------------------------

for i in range(1,11): # de la posición 1 hasta la 11 (excluye la 11)
    print(i)

#-------------------------------

for i in range(0,11,2): # de la posición 0 a la 11 (excluye), saltando de dos en dos
    print(i)

#-------------------------------

for i in range(0,16,2):
    if i == 2:
        print("Pasó por el número 2")
    else:
        print("No es número 2, es el número:",i)
    #print(i)