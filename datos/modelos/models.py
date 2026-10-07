from peewee import Model, CharField, TextField, IntegerField, DecimalField, SQL, AutoField, CompositeKey, DateTimeField
from datos.modelos.models import Producto
from datos.conexion import crear_conexion



database = crear_conexion()



class BaseModel(Model):
    class Meta:
        database = database

class Almacen(BaseModel):
    id_almacen = AutoField()
    id_direccion = IntegerField(index=True)
    nombre_almacen = CharField(max_length=50, null=True)

    class Meta:
        table_name = 'almacen'

class Categoria(BaseModel):
    descripcion_categoria = TextField(null=True)
    id_categoria = AutoField()
    nombre = CharField(max_length=35)

    class Meta:
        table_name = 'categoria'

class CategoriaProducto(BaseModel):
    gtin_producto = CharField(index=True, max_length=14)
    id_categoria = IntegerField()

    class Meta:
        table_name = 'categoria_producto'
        indexes = (
            (('id_categoria', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('id_categoria', 'gtin_producto')

class Direccion(BaseModel):
    calle = CharField(max_length=100)
    comuna = CharField(max_length=100)
    id_direccion = AutoField()
    numero_lugar = CharField(max_length=30)
    region = CharField(max_length=100)

    class Meta:
        table_name = 'direccion'

class Ingresos(BaseModel):
    cantidad = IntegerField()
    fecha_ingreso = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    gtin_producto = CharField(index=True, max_length=14, null=True)
    id_almacen = IntegerField(index=True)
    id_ingresos = AutoField()
    observacion = TextField(null=True)
    rut_proveedor = CharField(index=True, max_length=15, null=True)

    class Meta:
        table_name = 'ingresos'

class Producto(BaseModel):
    descripcion_producto = TextField(null=True)
    gtin = CharField(max_length=14, primary_key=True)
    nombre = CharField(max_length=50)
    perecible = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    precio_compra = DecimalField(decimal_places=2, max_digits=10, null=True)

    class Meta:
        table_name = 'producto'

class ProductoAlmacen(BaseModel):
    gtin_producto = CharField(max_length=14)
    id_almacen = IntegerField(index=True)
    stock = IntegerField()

    class Meta:
        table_name = 'producto_almacen'
        indexes = (
            (('gtin_producto', 'id_almacen'), True),
        )
        primary_key = CompositeKey('gtin_producto', 'id_almacen')

class Proveedor(BaseModel):
    correo = CharField(max_length=50, null=True)
    id_direccion = IntegerField(index=True)
    nombre = CharField(max_length=30, null=True)
    rut = CharField(max_length=15, primary_key=True)

    class Meta:
        table_name = 'proveedor'

class ProveedorProducto(BaseModel):
    gtin_producto = CharField(index=True, max_length=14)
    rut_proveedor = CharField(max_length=15)

    class Meta:
        table_name = 'proveedor_producto'
        indexes = (
            (('rut_proveedor', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('rut_proveedor', 'gtin_producto')

class Salida(BaseModel):
    cantidad = IntegerField()
    fecha_salida = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    gtin_producto = CharField(index=True, max_length=14, null=True)
    id_almacen = IntegerField(index=True)
    id_salidas = AutoField()
    motivo = CharField(null=True)

    class Meta:
        table_name = 'salida'

