from datos.repositorio.repo_producto import (listado_producto, stock_total_por_producto,
                                             buscar_producto, guardar_producto, eliminar_producto)
from datos.repositorio.categoria_producto import asignar_categoria
from datos.repositorio.repo_proveedor import asignar_proveedor
from datos.modelos.models import Producto
from prettytable import PrettyTable

def lista_producto():
    stock = stock_total_por_producto()

    # Un producto puede tener varios proveedores: se juntan en una sola fila
    productos = {}
    for gtin, nombre, descripcion, precio, perecible, vencimiento, proveedor in listado_producto():
        if gtin not in productos:
            productos[gtin] = [gtin, nombre, descripcion or "-", precio, perecible,
                               vencimiento or "-", stock.get(gtin, 0), []]
        if proveedor:
            productos[gtin][7].append(proveedor)

    if not productos:
        print("No hay productos registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["GTIN", "Producto", "Descripción", "Precio compra",
                         "Perecible", "Vencimiento", "Stock total", "Proveedor"]
    tabla.align = "l"
    for fila in productos.values():
        fila[7] = ", ".join(fila[7]) or "Sin proveedor"
        tabla.add_row(fila)

    print(tabla)

def existe_producto(gtin):
    return buscar_producto(gtin) is not None

def obtener_producto(gtin):
    return buscar_producto(gtin)

def crear_objeto_producto(gtin, nombre_producto, descripcion_producto, precio_compra, perecible,
                          fecha_vencimiento, id_categoria=None, rut_proveedor=None):
    nuevo_producto = Producto()
    nuevo_producto.gtin = gtin
    nuevo_producto.nombre_producto = nombre_producto
    nuevo_producto.descripcion_producto = descripcion_producto
    nuevo_producto.precio_compra = precio_compra
    nuevo_producto.perecible = perecible
    nuevo_producto.fecha_vencimiento = fecha_vencimiento
    if guardar_producto(nuevo_producto):
        if id_categoria is not None:
            asignar_categoria(gtin, id_categoria)
        if rut_proveedor:
            asignar_proveedor(gtin, rut_proveedor)

def borrar_producto(gtin):
    return eliminar_producto(gtin)