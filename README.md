# 📦 Sistema de Inventario con Python y SQLite

Aplicación desarrollada en Python para gestionar productos de un inventario utilizando una base de datos SQLite.

## Funcionalidades

* Agregar productos.
* Mostrar inventario.
* Buscar productos por ID.
* Modificar productos.
* Eliminar productos.
* Registrar ventas y actualizar stock.
* Mostrar productos con stock bajo.
* Calcular valor total del inventario.
* Generar reportes.
* Exportar inventario a Excel.

## Tecnologías utilizadas

* Python 3
* SQLite
* OpenPyXL

## Estructura del proyecto

```
Sistema-Inventario/

├── main.py
├── funciones.py
├── database.py
├── exportador.py
├── requirements.txt
└── README.md
```

## Instalación

Clonar el repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python main.py
```

## Características técnicas

* CRUD completo con SQLite.
* Consultas SQL.
* Validación de datos.
* Control de stock.
* Exportación automática a Excel.
* Código modular separado por responsabilidades.
