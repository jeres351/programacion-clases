from datos.modelos.models import Producto, Almacen, ProductoAlmacen
from peewee import JOIN

def stock_bajo(umbral):
    """Productos con stock <= umbral en algún almacén, o sin stock registrado."""
    return (Producto
            .select(Producto.gtin,
                    Producto.nombre_producto,
                    Almacen.nombre_almacen,
                    ProductoAlmacen.stock)
            .join(ProductoAlmacen, JOIN.LEFT_OUTER,
                  on=(Producto.gtin == ProductoAlmacen.gtin_producto))
            .join(Almacen, JOIN.LEFT_OUTER,
                  on=(ProductoAlmacen.id_almacen == Almacen.id_almacen))
            .where(ProductoAlmacen.stock.is_null() | (ProductoAlmacen.stock <= umbral))
            .order_by(ProductoAlmacen.stock, Producto.nombre_producto)
            .tuples())