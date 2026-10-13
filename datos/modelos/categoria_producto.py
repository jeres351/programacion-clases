from peewee import ForeignKeyField, CompositeKey
from datos.modelos.base_model import BaseModel
from datos.modelos.producto import Producto
from datos.modelos.categoria import Categoria

class CategoriaProducto(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_delete='CASCADE', on_update='CASCADE')
    id_categoria = ForeignKeyField(column_name='id_categoria', field='id_categoria', model=Categoria, on_delete='CASCADE', on_update='CASCADE')

    class Meta:
        table_name = 'categoria_producto'
        indexes = (
            (('id_categoria', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('id_categoria', 'gtin_producto')
