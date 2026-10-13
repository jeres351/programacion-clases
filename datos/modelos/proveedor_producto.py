from peewee import ForeignKeyField, CompositeKey
from datos.modelos.base_model import BaseModel
from datos.modelos.producto import Producto
from datos.modelos.proveedor import Proveedor

class ProveedorProducto(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_delete='CASCADE', on_update='CASCADE')
    rut_proveedor = ForeignKeyField(column_name='rut_proveedor', field='rut', model=Proveedor, on_delete='CASCADE', on_update='CASCADE')

    class Meta:
        table_name = 'proveedor_producto'
        indexes = (
            (('rut_proveedor', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('rut_proveedor', 'gtin_producto')
