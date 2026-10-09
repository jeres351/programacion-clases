from datos.modelos.models import Producto
from peewee import IntegrityError, OperationalError, PeeweeException

def listado_producto():
    productos = Producto.select()
    return productos

def guardar_producto(producto):
    try:
        producto_guardado = producto.save(force_insert=True)
        if producto_guardado == 1:
            print("Producto guardado correctamente. nombre del producto:", producto.nombre_producto)
    except IntegrityError as e:
        print(f"Error de clave única o foránea: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")