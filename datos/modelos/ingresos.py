from peewee import IntegerField, DateTimeField, ForeignKeyField, TextField, AutoField, SQL
from datos.modelos.base_model import BaseModel
from datos.modelos.producto import Producto
from datos.modelos.almacen import Almacen
from datos.modelos.proveedor import Proveedor

class Ingresos(BaseModel):
    cantidad_ingreso = IntegerField()
    fecha_ingreso = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_update='CASCADE')
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacen, on_update='CASCADE')
    id_ingresos = AutoField()
    observacion_ingreso = TextField(null=True)
    rut_proveedor = ForeignKeyField(column_name='rut_proveedor', field='rut', model=Proveedor, on_update='CASCADE')

    class Meta:
        table_name = 'ingresos'
