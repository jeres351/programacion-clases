from peewee import *
from datos.conexion import db



class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Direccion(BaseModel):
    calle = CharField()
    comuna = CharField()
    id_direccion = AutoField()
    numero_lugar = CharField()
    region = CharField()

    class Meta:
        table_name = 'direccion'

class Almacen(BaseModel):
    id_almacen = AutoField()
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direccion)
    nombre_almacen = CharField(null=True)

    class Meta:
        table_name = 'almacen'

class Categoria(BaseModel):
    descripcion_categoria = TextField(null=True)
    id_categoria = AutoField()
    nombre = CharField()

    class Meta:
        table_name = 'categoria'

class Producto(BaseModel):
    descripcion_producto = TextField(null=True)
    gtin = CharField(primary_key=True)
    nombre = CharField()
    perecible = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    precio_compra = DecimalField(null=True)

    class Meta:
        table_name = 'producto'

class CategoriaProducto(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto)
    id_categoria = ForeignKeyField(column_name='id_categoria', field='id_categoria', model=Categoria)

    class Meta:
        table_name = 'categoria_producto'
        indexes = (
            (('id_categoria', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('gtin_producto', 'id_categoria')

class Proveedor(BaseModel):
    correo = CharField(null=True)
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direccion)
    nombre = CharField(null=True)
    rut = CharField(primary_key=True)

    class Meta:
        table_name = 'proveedor'

class Ingresos(BaseModel):
    cantidad = IntegerField()
    fecha_ingreso = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, null=True)
    id_ingresos = AutoField()
    observacion = TextField(null=True)
    rut_proveedor = ForeignKeyField(column_name='rut_proveedor', field='rut', model=Proveedor, null=True)

    class Meta:
        table_name = 'ingresos'

class ProductoAlmacen(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto)
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacen)
    stock = IntegerField()

    class Meta:
        table_name = 'producto_almacen'
        indexes = (
            (('gtin_producto', 'id_almacen'), True),
        )
        primary_key = CompositeKey('gtin_producto', 'id_almacen')

class ProveedorProducto(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto)
    rut_proveedor = ForeignKeyField(column_name='rut_proveedor', field='rut', model=Proveedor)

    class Meta:
        table_name = 'proveedor_producto'
        indexes = (
            (('rut_proveedor', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('gtin_producto', 'rut_proveedor')

class Salida(BaseModel):
    cantidad = IntegerField()
    fecha_salida = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, null=True)
    id_salidas = AutoField()
    motivo = CharField(null=True)

    class Meta:
        table_name = 'salida'

