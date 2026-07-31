from database import agregar_producto, obtener_productos, buscar_producto, eliminar_producto, modificar_producto, actualizar_stock, obtener_stock_bajo, obtener_valor_inventario, contar_productos, obtener_producto_mas_caro, obtener_producto_mas_stock
from exportador import exportar_excel

def agregar_nuevo_producto():

    while True:

        nombre = input("Ingrese el nombre del producto: ").strip()

        if nombre != "":
            break

        print("El nombre no puede estar vacío.")

    while True:

        categoria = input("Ingrese la categoría: ").strip()

        if categoria != "":
            break

        print("La categoría no puede estar vacía.")

    while True:

        try:

            precio = float(input("Ingrese el precio: "))

            if precio > 0:
                break

            print("El precio debe ser mayor que cero.")

        except ValueError:

            print("Ingrese un número válido.")

    while True:

        try:

            stock = int(input("Ingrese el stock: "))

            if stock >= 0:
                break

            print("El stock no puede ser negativo.")

        except ValueError:

            print("Ingrese un número entero.")

    agregar_producto(
        nombre,
        categoria,
        precio,
        stock
    )

    print()

    print("Producto agregado correctamente.")

def mostrar_productos():

    productos = obtener_productos()

    if len(productos) == 0:

        print()

        print("No hay productos registrados.")

        return

    print()

    print("=" * 70)

    print("INVENTARIO")

    print("=" * 70)

    for producto in productos:

        print(f"ID: {producto[0]}")

        print(f"Nombre: {producto[1]}")

        print(f"Categoría: {producto[2]}")

        print(f"Precio: ${producto[3]:.2f}")

        print(f"Stock: {producto[4]}")

        print("-" * 70)


def buscar_producto_por_id():

    while True:

        try:

            id_producto = int(input("Ingrese el ID del producto: "))

            break

        except ValueError:

            print("Ingrese un número válido.")

    producto = buscar_producto(id_producto)

    if producto is None:

        print("No existe un producto con ese ID.")

        return


    print()

    print("=" * 50)

    print("PRODUCTO ENCONTRADO")

    print("=" * 50)

    print(f"ID: {producto[0]}")

    print(f"Nombre: {producto[1]}")

    print(f"Categoría: {producto[2]}")

    print(f"Precio: ${producto[3]:.2f}")

    print(f"Stock: {producto[4]}")

    print("=" * 50)


def eliminar_producto_por_id():

    while True:

        try:

            id_producto = int(input("Ingrese el ID del producto a eliminar: "))

            break

        except ValueError:

            print("Ingrese un número válido.")


    confirmacion = input(
        "¿Está seguro de eliminar este producto? (s/n): "
    ).lower()


    while confirmacion not in ["s", "n"]:

        confirmacion = input(
            "Ingrese s o n: "
        ).lower()


    if confirmacion == "n":

        print("Eliminación cancelada.")

        return


    resultado = eliminar_producto(id_producto)


    if resultado == 0:

        print("No existe un producto con ese ID.")

    else:

        print("Producto eliminado correctamente.")


def modificar_producto_por_id():

    while True:

        try:

            id_producto = int(input("Ingrese el ID del producto a modificar: "))

            break

        except ValueError:

            print("Ingrese un número válido.")


    nombre = input("Nuevo nombre: ").strip()

    while nombre == "":

        print("El nombre no puede estar vacío.")

        nombre = input("Nuevo nombre: ").strip()


    categoria = input("Nueva categoría: ").strip()

    while categoria == "":

        print("La categoría no puede estar vacía.")

        categoria = input("Nueva categoría: ").strip()


    while True:

        try:

            precio = float(input("Nuevo precio: "))

            if precio > 0:

                break

            print("El precio debe ser mayor que cero.")

        except ValueError:

            print("Ingrese un número válido.")


    while True:

        try:

            stock = int(input("Nuevo stock: "))

            if stock >= 0:

                break

            print("El stock no puede ser negativo.")

        except ValueError:

            print("Ingrese un número entero.")


    resultado = modificar_producto(
        id_producto,
        nombre,
        categoria,
        precio,
        stock
    )


    if resultado == 0:

        print("No existe un producto con ese ID.")

    else:

        print("Producto modificado correctamente.")


def registrar_venta():

    while True:

        try:

            id_producto = int(input("Ingrese ID del producto vendido: "))

            break

        except ValueError:

            print("Ingrese un número válido.")


    producto = buscar_producto(id_producto)


    if producto is None:

        print("Producto no encontrado.")

        return


    stock_actual = producto[4]


    print()

    print("Producto:")
    print(producto[1])

    print("Stock disponible:")
    print(stock_actual)


    while True:

        try:

            cantidad = int(input("Cantidad vendida: "))

            if cantidad > 0:

                break

            print("La cantidad debe ser mayor a cero.")

        except ValueError:

            print("Ingrese un número entero.")



    if cantidad > stock_actual:

        print("No hay suficiente stock.")

        return



    nuevo_stock = stock_actual - cantidad


    actualizar_stock(
        id_producto,
        nuevo_stock
    )


    print()

    print("Venta registrada correctamente.")

    print(f"Stock restante: {nuevo_stock}")


def mostrar_stock_bajo():

    while True:

        try:

            limite = int(input("Mostrar productos con stock menor o igual a: "))

            if limite >= 0:
                break

            print("El límite no puede ser negativo.")

        except ValueError:

            print("Ingrese un número entero.")


    productos = obtener_stock_bajo(limite)


    if len(productos) == 0:

        print()

        print("No hay productos con stock bajo.")

        return


    print()

    print("=" * 60)

    print("PRODUCTOS CON STOCK BAJO")

    print("=" * 60)


    for producto in productos:

        print(f"ID: {producto[0]}")
        print(f"Nombre: {producto[1]}")
        print(f"Categoría: {producto[2]}")
        print(f"Stock actual: {producto[4]}")

        print("-" * 60)

def mostrar_valor_inventario():

    total = obtener_valor_inventario()


    if total is None:

        total = 0


    print()

    print("=" * 50)

    print("VALOR TOTAL DEL INVENTARIO")

    print("=" * 50)

    print(f"${total:,.2f}")

    print("=" * 50)


def mostrar_reportes():

    cantidad = contar_productos()

    producto_caro = obtener_producto_mas_caro()

    producto_stock = obtener_producto_mas_stock()


    print()

    print("=" * 60)

    print("REPORTES DEL INVENTARIO")

    print("=" * 60)


    print()

    print("Cantidad total de productos:")

    print(cantidad)


    print()

    if producto_caro:

        print("Producto más caro:")

        print(producto_caro[1])

        print(f"Precio: ${producto_caro[3]:,.2f}")


    print()

    if producto_stock:

        print("Producto con mayor stock:")

        print(producto_stock[1])

        print(f"Cantidad: {producto_stock[4]} unidades")


    print()

    print("=" * 60)


def exportar_inventario():

    exportar_excel()


