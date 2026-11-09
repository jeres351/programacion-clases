from peewee import Model
from datos.conexion import crear_conexion

db = crear_conexion()

class BaseModel(Model):
    class Meta:
        database = db
