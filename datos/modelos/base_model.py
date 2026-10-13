from peewee import Model
from datos.conexion import crear_conexion

# Una sola conexión compartida por todos los modelos
# (necesario para que las transacciones abarquen varias tablas)
db = crear_conexion()

class BaseModel(Model):
    class Meta:
        database = db
