from datos.repositorio.repo_producto import listado_producto, guardar_producto
from datos.modelos.models import Producto, Proveedor, ProveedorProducto
from prettytable import PrettyTable
def lista_producto():
    query = (ProveedorProducto
             .select(ProveedorProducto, Producto, Proveedor)
             .join(Producto)
             .switch(ProveedorProducto)
             .join(Proveedor))

    tabla = PrettyTable()
    tabla.field_names = ["GTIN", "Producto", "Descripción", "Precio compra",
                         "Perecible", "Vencimiento", "Proveedor"]

    for pp in query:
        p = pp.gtin_producto
        tabla.add_row([p.gtin,
                       p.nombre_producto,
                       p.descripcion_producto,
                       p.precio_compra,
                       p.perecible,
                       p.fecha_vencimiento,
                       pp.rut_proveedor.nombre_proveedor])

    print(tabla)

def crear_objeto_producto(gtin, nombre_producto, descripcion_producto, precio_compra, perecible, fecha_vencimiento):
    nuevo_producto = Producto()
    nuevo_producto.gtin = gtin
    nuevo_producto.nombre_producto = nombre_producto
    nuevo_producto.descripcion_producto = descripcion_producto
    nuevo_producto.precio_compra = precio_compra
    nuevo_producto.perecible = perecible
    nuevo_producto.fecha_vencimiento = fecha_vencimiento
    guardar_producto(nuevo_producto)