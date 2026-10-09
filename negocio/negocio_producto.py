from datos.repositorio.repo_producto import listado_producto, guardar_producto
from datos.modelos.models import Producto
from prettytable import PrettyTable
def lista_producto():
    tabla_producto = PrettyTable()
    tabla_producto.field_names = ['gtin', 'nombre_producto', 'descripcion_producto', 'precio_compra', 'perecible', 'fecha_vencimiento']
    productos = listado_producto()
    for producto in productos:
        tabla_producto.add_row([producto.gtin, producto.nombre_producto, producto.descripcion_producto, producto.precio_compra, producto.perecible, producto.fecha_vencimiento])
    print(tabla_producto)


def crear_objeto_producto(gtin, nombre_producto, descripcion_producto, precio_compra, perecible, fecha_vencimiento):
    nuevo_producto = Producto()
    nuevo_producto.gtin = gtin
    nuevo_producto.nombre_producto = nombre_producto
    nuevo_producto.descripcion_producto = descripcion_producto
    nuevo_producto.precio_compra = precio_compra
    nuevo_producto.perecible = perecible
    nuevo_producto.fecha_vencimiento = fecha_vencimiento
    guardar_producto(nuevo_producto)