from datos.modelos.producto import Producto

def listado_producto():
    lista_productos = Producto.select()
    