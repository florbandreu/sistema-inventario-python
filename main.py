from database import crear_base_datos
from funciones import *

crear_base_datos()

while True:

    print()

    print("1. Agregar producto")

    print("2. Mostrar productos")

    print("3. Buscar producto")

    print("4. Eliminar producto")

    print("5. Modificar producto")

    print("6. Registrar venta")

    print("7. Mostrar stock bajo")

    print("8. Valor total inventario")

    print("9. Reportes")

    print("10. Exportar Excel")

    print("11. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        agregar_nuevo_producto()

    elif opcion == "2":

        mostrar_productos()

    elif opcion == "3":

        buscar_producto_por_id()

    elif opcion == "4":
    
        eliminar_producto_por_id()

    elif opcion == "5":
    
        modificar_producto_por_id()

    elif opcion == "6":
        
        registrar_venta()

    elif opcion == "7":
            
        mostrar_stock_bajo()

    elif opcion == "8":
                
        mostrar_valor_inventario()

    elif opcion == "9":
                    
        mostrar_reportes()

    elif opcion == "10":
                        
        exportar_inventario()

    elif opcion == "11":
    
        print("Programa finalizado.")

        break

    else:

        print("Opción inválida.")