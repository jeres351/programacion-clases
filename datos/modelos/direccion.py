from peewee import CharField, AutoField
from datos.modelos.base_model import BaseModel

class Direccion(BaseModel):
    calle = CharField(max_length=100)
    comuna = CharField(max_length=100)
    id_direccion = AutoField()
    numero_lugar = CharField(max_length=30)
    region = CharField(max_length=100)

    class Meta:
        table_name = 'direccion'
