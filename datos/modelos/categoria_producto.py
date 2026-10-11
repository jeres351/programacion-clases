from peewee import Model, ForeignKeyField, CompositeKey
from datos.modelos.models import Producto, Categoria
from datos.conexion import crear_conexion
database = crear_conexion()

class BaseModel(Model):
    class Meta:
        database = crear_conexion()


class CategoriaProducto(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_delete='CASCADE', on_update='CASCADE')
    id_categoria = ForeignKeyField(column_name='id_categoria', field='id_categoria', model=Categoria, on_delete='CASCADE', on_update='CASCADE')

    class Meta:
        table_name = 'categoria_producto'
        indexes = (
            (('id_categoria', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('id_categoria', 'gtin_producto')