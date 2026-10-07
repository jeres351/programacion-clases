from datos.modelos.producto import Producto
from peewee import IntegrityError, OperationalError, PeeweeException


def listado_producto():
    lista_productos = Producto.select()
    if lista_productos:
        return lista_productos
    
def guardar_producto(producto:Producto):
    try:
        producto_guardado = producto.save()
        if producto_guardado == 1:
            print(f'Producto guardado con éxito. gtin: {pais.id_pais}')
    except IntegrityError as e:
        print(f"Error de clave única o foránea: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    
    