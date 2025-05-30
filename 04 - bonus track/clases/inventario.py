class Inventario:
    def __init__(self):
        self.lista_de_prodctos = []

    def agregar_producto(self, producto):
        self.lista_de_prodctos.append(producto)

    def actualizar_inventario(self, producto, cantidad):
        for prod in self.lista_de_prodctos:
            if prod.nombre == producto.nombre:
                prod.actualizar_cantidad(cantidad)

    def generar_alerta(self, umbral_minimo):
        alertas = [
            prod.nombre
            for prod in self.lista_de_prodctos
            if prod.cantidad < umbral_minimo
        ]
        return (
            f"Productos por debajo del umbral: {', '.join(alertas)}"
            if alertas
            else "No hay ningún producto por debajo del umbral mínimo determinado"
        )
