from clases.mago import Mago

merlin = Mago("Merlín", ["Bola de fuego", "Rayo"])
gandalf = Mago(
    "Gandalf", ["Llamar a las aguilas cuando terminó la película", "Bola de fuego"]
)

print(merlin)  # Devuelve el método __str__ que habíamos generado en la clase
print(len(merlin))  # Devuelve el método __len__ que habíamos generado en la clase

print(gandalf)  # Devuelve el método __str__ que habíamos generado en la clase
print(len(gandalf))  # Devuelve el método __len__ que habíamos generado en la clase

print(
    merlin == gandalf
)  # Devuelve un booleano resultado de la comparación usando los criterios que definimos en el método __eq__

copia_merlin = Mago("Merlín", ["Bola de fuego", "Rayo"])

print(
    merlin == copia_merlin
)  # Devuelve un booleano resultado de la comparación usando los criterios que definimos en el método __eq__

mago_combinado = merlin + gandalf
print(mago_combinado)