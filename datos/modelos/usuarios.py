from datetime import datetime
from peewee import AutoField, CharField, BooleanField, DateTimeField
from datos.modelos.base_model import BaseModel


class Usuarios(BaseModel):
    id_usuario = AutoField()
    nombre_usuario = CharField(max_length=25)
    apellido_usuario = CharField(max_length=25)
    correo_usuario = CharField(max_length=255, unique=True)
    contrasena_usuario = CharField(max_length=72)
    fecha_incorporacion = DateTimeField(default=datetime.now)
    habilitado = BooleanField(default=True)

    class Meta:
        table_name = 'usuarios'