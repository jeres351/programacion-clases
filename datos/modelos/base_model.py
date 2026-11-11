from peewee import Model, BooleanField, DateTimeField
from datos.conexion import crear_conexion

db = crear_conexion()

class BaseModel(Model):
    class Meta:
        database = db

class ModeloBorradoLogico(BaseModel):
    activo = BooleanField(default=True)
    fecha_eliminacion = DateTimeField(null=True)