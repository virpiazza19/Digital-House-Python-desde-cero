# Funciones para interfaz de consola

from clases.mascota import Perro, Gato
from clases.cliente import Cliente
from clases.venta import Venta
from clases.producto import Producto
from clases.inventario import Inventario


def registrar_mascota():
    tipo = input("Ingrese el tipo de mascota (Perro/Gato): ").strip().lower()
    nombre = input("Nombre de la mascota: ")
    edad = int(input("Edad de la mascota: "))
    salud = input("Estado de salud de la mascota: ")
    precio = float(input("Precio de atención de la mascota: "))

    if tipo == "perro":
        raza = input("Raza del perro: ")
        nivel_de_energia = input("Nivel de energía del perro: ")
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_de_energia)
    elif tipo == "gato":
        raza = input("Raza del gato: ")
        independencia = input("Nivel de independencia del gato: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no reconocido")
        return None
    return mascota


def registrar_cliente():
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección del cliente: ")
    telefono = input("Teléfono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)

    return cliente


def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))
    producto = Producto(nombre, categoria, precio, cantidad)

    return producto


def registrar_venta(clientes, inventario):
    nombre_cliente = input("Nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado")
        return

    productos = []

    while True:
        nombre_producto = input("Nombre del producto (deje vacío para finalizar): ")
        if not nombre_producto:
            break
        producto = next(
            (p for p in inventario.lista_de_productos if p.nombre == nombre_producto),
            None,
        )
        if producto:
            productos.append(producto)
        else:
            print("Producto no encontrado")
            
    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print("La venta ha sido registrada exitosamente")
    else:
        print("No se han registrado productos para la venta")


# \ -> alt+92
# \n -> salto de línea
# \b -> backspace


def mostrar_menu():
    print("\n --- Menú de gestión de Patas Felices")
    print("1. Registrar Mascota")
    print("2. Registrar Cliente")
    print("3. Registrar Producto")
    print("4. Registrar Venta")
    print("5. Mostrar información acerca de Mascota")
    print("6. Mostrar información acerca de Cliente")
    print("7. Mostrar información acerca de Producto")
    print("8. Generar alerta de inventario")
    print("9. Salir")


def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # 1. Registrar Mascota
        if opcion == "1":
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print("Mascota registrada con éxito!")

        # 2. Registrar Cliente
        elif opcion == "2":
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print("Cliente registrado con éxito!")

        # 3. Registrar Producto
        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print("Producto registrado con éxito!")

        # 4. Registrar Venta
        elif opcion == "4":
            registrar_venta(clientes, inventario)

        # 5. Mostrar información acerca de Mascota
        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())

        # 6. Mostrar información acerca de Cliente
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_informacion())

        # 7. Mostrar información acerca de Producto
        elif opcion == "7":
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_informacion())

        # 8. Generar alerta de inventario
        elif opcion == "8":
            umbral_minimo = int(input("Ingrese el umbral mínimo: "))
            print(inventario.generar_alerta(umbral_minimo))
        
        # 9. Salir
        elif opcion == "9":
            print("Saliendo del sistema ¡Gracias por usar Patas Felices App!")
            break
        else:
            print("Opción no válida, intente nuevamente")
            
if __name__ == "__main__":
    main()
