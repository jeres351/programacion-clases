from datos.repositorios.repo_pais import listado_producto, guardar_producto
from datos.modelos.pais import Pais
from prettytable import PrettyTable

def lista_producto():
    tabla_producto = PrettyTable()
    tabla_producto.field_names = ['gtin', 'nombre_producto', 'descripcion_producto', 'precio_compra', 'perecible', 'fecha_vencimiento']
    productos = listado_producto()
    for producto in productos:
        tabla_producto.add_row([producto.gtin, producto.producto_nombre, producto.producto_descripcion, producto.precio_compra, producto.perecible, producto.fecha_vencimiento])
    print(tabla_producto)


def crear_objeto_pais(no, nacionalidad, iso2, iso3):
    nuevo_pais = Pais()
    nuevo_pais.pais = pais
    nuevo_pais.nacionalidad = nacionalidad
    nuevo_pais.iso2 = iso2
    nuevo_pais.iso3 = iso3
    guardar_pais(nuevo_pais)