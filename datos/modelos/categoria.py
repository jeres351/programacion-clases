from peewee import TextField, AutoField, CharField
from datos.modelos.base_model import BaseModel

class Categoria(BaseModel):
    descripcion_categoria = TextField(null=True)
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=35)

    class Meta:
        table_name = 'categoria'
