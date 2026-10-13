from peewee import IntegerField, DateTimeField, ForeignKeyField, AutoField, CharField, SQL
from datos.modelos.base_model import BaseModel
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen

class Salida(BaseModel):
    cantidad_salida = IntegerField()
    fecha_salida = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_update='CASCADE')
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacen, on_update='CASCADE')
    id_salidas = AutoField()
    motivo_salida = CharField(null=True)

    class Meta:
        table_name = 'salida'
