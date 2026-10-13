from peewee import TextField, DateField, CharField, DecimalField
from datos.modelos.base_model import BaseModel

class Producto(BaseModel):
    descripcion_producto = TextField(null=True)
    fecha_vencimiento = DateField(null=True)
    gtin = CharField(max_length=14, primary_key=True)
    nombre_producto = CharField(max_length=50)
    perecible = CharField(max_length=2)
    precio_compra = DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        table_name = 'producto'
