from negocio.negocio_producto import lista_producto, existe_producto, obtener_producto
from negocio.negocio_operacion import (mostrar_almacenes, existe_almacen, obtener_stock,registrar_entrada, registrar_salida_producto, mostrar_historial)
from negocio.negocio_proveedor import mostrar_proveedores, existe_proveedor
from auxiliares.entradas import pedir_texto, pedir_gtin, pedir_entero
sonar = "No existe un producto con ese GTIN."

def solicitar_datos_entrada():
    print("\n--- Registrar entrada ---")
    lista_producto()
    gtin = pedir_gtin("GTIN del producto: ")
    if not existe_producto(gtin):
        print(sonar)
        return

    if not mostrar_almacenes():
        return
    id_almacen = pedir_entero("ID del almacén: ")
    if not existe_almacen(id_almacen):
        print("No existe un almacén con ese ID.")
        return

    if not mostrar_proveedores():
        return
    rut_proveedor = pedir_texto("RUT del proveedor: ", 15)
    if not existe_proveedor(rut_proveedor):
        print("No existe un proveedor con ese RUT.")
        return

    cantidad = pedir_entero("Cantidad que ingresa: ", 1)
    observacion = pedir_texto("Observación (opcional): ", None, False)

    registrar_entrada(gtin, id_almacen, rut_proveedor, cantidad, observacion)

def solicitar_datos_salida():
    print("\n--- Registrar salida ---")
    lista_producto()
    gtin = pedir_gtin("GTIN del producto: ")
    if not existe_producto(gtin):
        print("No existe un producto con ese GTIN.")
        return

    if not mostrar_almacenes():
        return
    id_almacen = pedir_entero("ID del almacén: ")
    if not existe_almacen(id_almacen):
        print("No existe un almacén con ese ID.")
        return

    disponible = obtener_stock(gtin, id_almacen)
    print(f"Stock disponible en ese almacén: {disponible}")
    if disponible == 0:
        print("No hay stock para registrar una salida.")
        return

    cantidad = pedir_entero("Cantidad que sale: ", 1, disponible)
    motivo = pedir_texto("Motivo (ej: Venta, Merma) (opcional): ", 255, False)

    registrar_salida_producto(gtin, id_almacen, cantidad, motivo)

def solicitar_historial():
    print("\n--- Historial de movimientos ---")
    gtin = pedir_texto("GTIN para filtrar (Enter = todos): ", 14, False)
    if gtin and obtener_producto(gtin) is None:
        print(sonar)
        return
    mostrar_historial(gtin)