from datetime import datetime
from datos.modelos.models import (Producto, Proveedor, ProveedorProducto,
                                  ProductoAlmacen, CategoriaProducto)
from peewee import JOIN, fn, IntegrityError, OperationalError, PeeweeException

def listado_producto():
    """Productos activos con su proveedor activo (None si no tiene). Devuelve tuplas."""
    return (Producto
            .select(Producto.gtin,
                    Producto.nombre_producto,
                    Producto.descripcion_producto,
                    Producto.precio_compra,
                    Producto.perecible,
                    Producto.fecha_vencimiento,
                    Proveedor.nombre_proveedor)
            .join(ProveedorProducto, JOIN.LEFT_OUTER,
                  on=(Producto.gtin == ProveedorProducto.gtin_producto))
            .join(Proveedor, JOIN.LEFT_OUTER,
                  on=((ProveedorProducto.rut_proveedor == Proveedor.rut) &
                      (Proveedor.activo == True)))
            .where(Producto.activo == True)
            .order_by(Producto.nombre_producto)
            .tuples())

def stock_total_por_producto():
    """Devuelve {gtin: stock total sumando todos los almacenes}."""
    query = (ProductoAlmacen
             .select(ProductoAlmacen.gtin_producto, fn.SUM(ProductoAlmacen.stock))
             .group_by(ProductoAlmacen.gtin_producto)
             .tuples())
    return {gtin: int(total) for gtin, total in query}

def buscar_producto(gtin):
    """Solo productos activos."""
    return Producto.get_or_none((Producto.gtin == gtin) & (Producto.activo == True))

def buscar_producto_eliminado(gtin):
    return Producto.get_or_none((Producto.gtin == gtin) & (Producto.activo == False))

def guardar_producto(producto):
    try:
        producto_guardado = producto.save(force_insert=True)
        if producto_guardado == 1:
            print("Producto guardado correctamente. nombre del producto:", producto.nombre_producto)
            return True
    except IntegrityError as e:
        print(f"Error de clave única o foránea: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    return False

def eliminar_producto(gtin):
    try:
        filas = (Producto
                 .update(activo=False, fecha_eliminacion=datetime.now())
                 .where((Producto.gtin == gtin) & (Producto.activo == True))
                 .execute())
        if filas == 1:
            print("Producto eliminado correctamente.")
        else:
            print("No existe un producto activo con ese GTIN.")
        return filas
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")

def restaurar_producto(gtin):
    try:
        filas = (Producto
                 .update(activo=True, fecha_eliminacion=None)
                 .where((Producto.gtin == gtin) & (Producto.activo == False))
                 .execute())
        if filas == 1:
            print("Producto reactivado correctamente.")
        return filas
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")


def productos_por_categoria(id_categoria):
    return (Producto
            .select()
            .join(CategoriaProducto)
            .where((CategoriaProducto.id_categoria == id_categoria) &
                   (Producto.activo == True)))
