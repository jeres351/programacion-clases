from peewee import TextField, AutoField, CharField, ForeignKeyField
from datos.modelos.base_model import BaseModel
from datos.modelos.direccion import Direccion

class Almacen(BaseModel):
    id_almacen = AutoField()
    id_direccion = ForeignKeyField(
        column_name='id_direccion', 
        field='id_direccion', 
        model=Direccion, 
        on_update='CASCADE')
    nombre_almacen = CharField(max_length=50)

    class Meta:
        table_name = 'almacen'
