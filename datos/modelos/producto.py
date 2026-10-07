from peewee import Model, CharField, TextField, IntegerField, DecimalField, SQL 
from datos.conexion import crear_conexion 

#esto esta incompleto, es un borrador de lo que vimos en clases POO.

database = crear_conexion()



class BaseModel(Model):
    class Meta:
        database = database
        
        
class Producto(BaseModel):
    descripcion_producto = TextField(null=True)
    gtin = CharField(max_length=14, primary_key=True)
    nombre = CharField(max_length=50)
    perecible = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    precio_compra = DecimalField(decimal_places=2, max_digits=10, null=True)

    class Meta:
        table_name = 'producto'