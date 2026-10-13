from peewee import CharField, ForeignKeyField
from datos.modelos.base_model import BaseModel
from datos.modelos.direccion import Direccion

class Proveedor(BaseModel):
    correo_proveedor = CharField(max_length=50, null=True)
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direccion, on_update='CASCADE')
    nombre_proveedor = CharField(max_length=30)
    rut = CharField(max_length=15, primary_key=True)
    telefono_proveedor = CharField(max_length=15, null=True)

    class Meta:
        table_name = 'proveedor'
