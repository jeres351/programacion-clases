from datos.modelos.models import (BaseModel, Producto, Proveedor, Almacen, Direccion,
                                  Ingresos, Salida, ProductoAlmacen)
from peewee import IntegrityError, OperationalError, PeeweeException

db = BaseModel._meta.database


class StockInsuficiente(Exception):
    pass


def listado_almacenes():
    return (Almacen
            .select(Almacen, Direccion)
            .join(Direccion)
            .order_by(Almacen.id_almacen))

def buscar_almacen(id_almacen):
    return Almacen.get_or_none(Almacen.id_almacen == id_almacen)

def stock_disponible(gtin, id_almacen):
    fila = (ProductoAlmacen
            .select(ProductoAlmacen.stock)
            .where((ProductoAlmacen.gtin_producto == gtin) &
                   (ProductoAlmacen.id_almacen == id_almacen))
            .tuples()
            .first())
    return fila[0] if fila else 0

def registrar_ingreso(gtin, id_almacen, rut_proveedor, cantidad, observacion):
    """Guarda el ingreso y suma el stock en una sola transacción."""
    try:
        with db.atomic():
            Ingresos.create(gtin_producto=gtin,
                            id_almacen=id_almacen,
                            rut_proveedor=rut_proveedor,
                            cantidad_ingreso=cantidad,
                            observacion_ingreso=observacion)
            filas = (ProductoAlmacen
                     .update(stock=ProductoAlmacen.stock + cantidad)
                     .where((ProductoAlmacen.gtin_producto == gtin) &
                            (ProductoAlmacen.id_almacen == id_almacen))
                     .execute())
            if filas == 0:
                ProductoAlmacen.create(gtin_producto=gtin, id_almacen=id_almacen, stock=cantidad)
        print("Entrada registrada correctamente.")
        return True
    except IntegrityError as e:
        print(f"No se pudo registrar la entrada (revise GTIN, almacén y proveedor): {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    return False

def registrar_salida(gtin, id_almacen, cantidad, motivo):
    """Guarda la salida y descuenta el stock en una sola transacción."""
    try:
        with db.atomic():
            filas = (ProductoAlmacen
                     .update(stock=ProductoAlmacen.stock - cantidad)
                     .where((ProductoAlmacen.gtin_producto == gtin) &
                            (ProductoAlmacen.id_almacen == id_almacen) &
                            (ProductoAlmacen.stock >= cantidad))
                     .execute())
            if filas == 0:
                raise StockInsuficiente()
            Salida.create(gtin_producto=gtin,
                          id_almacen=id_almacen,
                          cantidad_salida=cantidad,
                          motivo_salida=motivo)
        print("Salida registrada correctamente.")
        return True
    except StockInsuficiente:
        print("Stock insuficiente en ese almacén.")
    except IntegrityError as e:
        print(f"No se pudo registrar la salida: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    return False

def historial_ingresos(gtin=None):
    query = (Ingresos
             .select(Ingresos.fecha_ingreso,
                     Producto.gtin,
                     Producto.nombre_producto,
                     Almacen.nombre_almacen,
                     Ingresos.cantidad_ingreso,
                     Proveedor.nombre_proveedor,
                     Ingresos.observacion_ingreso)
             .join(Producto, on=(Ingresos.gtin_producto == Producto.gtin))
             .switch(Ingresos)
             .join(Almacen, on=(Ingresos.id_almacen == Almacen.id_almacen))
             .switch(Ingresos)
             .join(Proveedor, on=(Ingresos.rut_proveedor == Proveedor.rut)))
    if gtin:
        query = query.where(Producto.gtin == gtin)
    return query.tuples()

def historial_salidas(gtin=None):
    query = (Salida
             .select(Salida.fecha_salida,
                     Producto.gtin,
                     Producto.nombre_producto,
                     Almacen.nombre_almacen,
                     Salida.cantidad_salida,
                     Salida.motivo_salida)
             .join(Producto, on=(Salida.gtin_producto == Producto.gtin))
             .switch(Salida)
             .join(Almacen, on=(Salida.id_almacen == Almacen.id_almacen)))
    if gtin:
        query = query.where(Producto.gtin == gtin)
    return query.tuples()
