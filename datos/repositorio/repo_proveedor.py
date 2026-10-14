from datos.modelos.models import (BaseModel, Proveedor, Direccion, Almacen, ProveedorProducto)
from peewee import IntegrityError, OperationalError, PeeweeException

db = BaseModel._meta.database


def listado_proveedores():
    return (Proveedor
            .select(Proveedor, Direccion)
            .join(Direccion)
            .order_by(Proveedor.nombre_proveedor))

def buscar_proveedor(rut):
    return Proveedor.get_or_none(Proveedor.rut == rut)

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
        with db.atomic():
            proveedor = Proveedor.get_or_none(Proveedor.rut == rut)
            if proveedor is None:
                print("No existe un proveedor con ese RUT.")
                return 0
            id_direccion = proveedor.id_direccion_id
            filas = Proveedor.delete().where(Proveedor.rut == rut).execute()

            # La dirección se borra solo si ya nadie más la usa
            en_uso = (Proveedor.select().where(Proveedor.id_direccion == id_direccion).exists() or
                      Almacen.select().where(Almacen.id_direccion == id_direccion).exists())
            if not en_uso:
                Direccion.delete().where(Direccion.id_direccion == id_direccion).execute()
        print("Proveedor eliminado correctamente.")
        return filas
    except IntegrityError as e:
        print(f"No se puede eliminar, el proveedor tiene ingresos registrados: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")