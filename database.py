import sqlite3


def crear_base_datos():

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            nombre TEXT NOT NULL,

            categoria TEXT NOT NULL,

            precio REAL NOT NULL,

            stock INTEGER NOT NULL
        )
    """)

    conexion.commit()

    conexion.close()


def agregar_producto(nombre, categoria, precio, stock):

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos(
            nombre,
            categoria,
            precio,
            stock
        )
        VALUES (?, ?, ?, ?)
    """, (nombre, categoria, precio, stock))

    conexion.commit()

    conexion.close()


def obtener_productos():

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM productos
        ORDER BY nombre
    """)

    productos = cursor.fetchall()

    conexion.close()

    return productos


def buscar_producto(id_producto):

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM productos
        WHERE id = ?
    """, (id_producto,))

    producto = cursor.fetchone()

    conexion.close()

    return producto

def eliminar_producto(id_producto):

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM productos
        WHERE id = ?
    """, (id_producto,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    conexion.close()

    return filas_afectadas


def modificar_producto(id_producto, nombre, categoria, precio, stock):

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE productos
        SET nombre = ?,
            categoria = ?,
            precio = ?,
            stock = ?
        WHERE id = ?
    """, (nombre, categoria, precio, stock, id_producto))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    conexion.close()

    return filas_afectadas

def actualizar_stock(id_producto, nuevo_stock):

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE productos
        SET stock = ?
        WHERE id = ?
    """, (nuevo_stock, id_producto))


    conexion.commit()

    filas_afectadas = cursor.rowcount

    conexion.close()

    return filas_afectadas

def obtener_stock_bajo(limite):

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM productos
        WHERE stock <= ?
        ORDER BY stock ASC
    """, (limite,))

    productos = cursor.fetchall()

    conexion.close()

    return productos


def obtener_valor_inventario():

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT SUM(precio * stock)
        FROM productos
    """)

    total = cursor.fetchone()[0]

    conexion.close()

    return total

def contar_productos():

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM productos
    """)

    cantidad = cursor.fetchone()[0]

    conexion.close()

    return cantidad

def obtener_producto_mas_caro():

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM productos
        ORDER BY precio DESC
        LIMIT 1
    """)

    producto = cursor.fetchone()

    conexion.close()

    return producto


def obtener_producto_mas_stock():

    conexion = sqlite3.connect("inventario.db")

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM productos
        ORDER BY stock DESC
        LIMIT 1
    """)

    producto = cursor.fetchone()

    conexion.close()

    return producto