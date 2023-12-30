
productos = {
    'Leche': 50,
    'Galletas': 35,
    'Gaseosa': 87,
    'Huevos': 66,
    'Aceite': 110,
    'Pan': 20
}


carrito = {}


def agregar_producto():
    print("Productos disponibles:")
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")

    producto = input("Ingrese el nombre del producto que desea agregar: ")
    if producto in productos:
        if producto in carrito:
            carrito[producto] += 1
        else:
            carrito[producto] = 1
        print(f"{producto} agregado al carrito.")
    else:
        print("El producto ingresado no está disponible.")


def eliminar_producto():
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        print("Productos en el carrito:")
        for producto, cantidad in carrito.items():
            print(f"{producto}: {cantidad}")

        producto = input("Ingrese el nombre del producto que desea eliminar: ")
        if producto in carrito:
            carrito[producto] -= 1
            if carrito[producto] == 0:
                del carrito[producto]
            print(f"{producto} eliminado del carrito.")
        else:
            print("El producto ingresado no está en el carrito.")


def ver_lista_compras():
    if len(carrito) == 0:
        print("El carrito está vacío.")
    else:
        print("Productos en el carrito:")
        total = 0
        for producto, cantidad in carrito.items():
            precio = productos[producto] * cantidad
            print(f"{producto}: {cantidad} x ${productos[producto]} = ${precio}")
            total += precio
        print(f"Total a pagar: ${total}")


def finalizar_compra():
    ver_lista_compras()
    print("¡Gracias por su compra!")
    exit()


while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver lista de compras")
    print("4. Finalizar compra")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        eliminar_producto()
    elif opcion == '3':
        ver_lista_compras()
    elif opcion == '4':
        finalizar_compra()
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")