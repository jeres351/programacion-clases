from peewee import ForeignKeyField, IntegerField, CompositeKey, SQL
from datos.modelos.base_model import BaseModel
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen

class ProductoAlmacen(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_delete='CASCADE', on_update='CASCADE')
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacen, on_delete='CASCADE', on_update='CASCADE')
    stock = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'producto_almacen'
        indexes = (
            (('gtin_producto', 'id_almacen'), True),
        )
        primary_key = CompositeKey('gtin_producto', 'id_almacen')
