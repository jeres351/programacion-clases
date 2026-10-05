from peewee import Model
from datos.modelos.models import Producto

#esto esta incompleto, es un borrador de lo que vimos en clases POO.

database = 



class Producto(BaseModel):
    gtin = CharField(max_length=14, primary_key=True)


    class Meta:
        table_name = "producto"