from datetime import datetime
from datos.modelos.models import (BaseModel, Proveedor, Direccion, ProveedorProducto)
from peewee import IntegrityError, OperationalError, PeeweeException

db = BaseModel._meta.database


def listado_proveedores():
    return (Proveedor
            .select(Proveedor, Direccion)
            .join(Direccion)
            .where(Proveedor.activo == True)
            .order_by(Proveedor.nombre_proveedor))

def buscar_proveedor(rut):
    """Solo proveedores activos."""
    return Proveedor.get_or_none((Proveedor.rut == rut) & (Proveedor.activo == True))

def buscar_proveedor_eliminado(rut):
    return Proveedor.get_or_none((Proveedor.rut == rut) & (Proveedor.activo == False))

def guardar_proveedor(proveedor, direccion):
    """Guarda la dirección y el proveedor juntos (si falla uno, no se guarda ninguno)."""
    try:
        with db.atomic():
            direccion.save()
            proveedor.id_direccion = direccion.id_direccion
            proveedor.save(force_insert=True)
        print("Proveedor guardado correctamente. nombre del proveedor:", proveedor.nombre_proveedor)
        return True
    except IntegrityError as e:
        print(f"Error de clave única o foránea (¿el RUT ya existe?): {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    return False

def asignar_proveedor(gtin, rut):
    try:
        ProveedorProducto.create(gtin_producto=gtin, rut_proveedor=rut)
        print("Proveedor asignado al producto.")
        return True
    except IntegrityError as e:
        print(f"No se pudo asignar el proveedor: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    return False

def eliminar_proveedor(rut):
    try:
        filas = (Proveedor
                 .update(activo=False, fecha_eliminacion=datetime.now())
                 .where((Proveedor.rut == rut) & (Proveedor.activo == True))
                 .execute())
        if filas == 1:
            print("Proveedor eliminado correctamente.")
        else:
            print("No existe un proveedor activo con ese RUT.")
        return filas
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")

def restaurar_proveedor(rut):
    try:
        filas = (Proveedor
                 .update(activo=True, fecha_eliminacion=None)
                 .where((Proveedor.rut == rut) & (Proveedor.activo == False))
                 .execute())
        if filas == 1:
            print("Proveedor reactivado correctamente.")
        return filas
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")