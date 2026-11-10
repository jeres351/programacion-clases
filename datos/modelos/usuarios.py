from peewee import CharField, BooleanField, IntegerField
from datos.modelos.base_model import BaseModel

class Usuarios(BaseModel):
    id_usuario = IntegerField(column_name='id_usuario', unique=True, null=False)
    correo_usuario = CharField(column_name='correo_usuario', max_length=100, primary_key=True)
    contrasena_usuario = CharField(column_name='contrasena_usuario', max_length=60)
    habilitado = BooleanField(default=True,null=False)

    class Meta:
        table_name = 'usuarios'