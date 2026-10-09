from peewee import Model, TextField, DateField, CharField, DecimalField, AutoField, ForeignKeyField, IntegerField, DateTimeField, CompositeKey, SQL
from datos.conexion import crear_conexion



class BaseModel(Model):
    class Meta:
        database = crear_conexion()

class Direccion(BaseModel):
    calle = CharField(max_length=100)
    comuna = CharField(max_length=100)
    id_direccion = AutoField()
    numero_lugar = CharField(max_length=30)
    region = CharField(max_length=100)

    class Meta:
        table_name = 'direccion'

class Almacen(BaseModel):
    id_almacen = AutoField()
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direccion, on_update='CASCADE')
    nombre_almacen = CharField(max_length=50)

    class Meta:
        table_name = 'almacen'

class Categoria(BaseModel):
    descripcion_categoria = TextField(null=True)
    id_categoria = AutoField()
    nombre_categoria = CharField(max_length=35)

    class Meta:
        table_name = 'categoria'

class Producto(BaseModel):
    descripcion_producto = TextField(null=True)
    fecha_vencimiento = DateField(null=True)
    gtin = CharField(max_length=14, primary_key=True)
    nombre_producto = CharField(max_length=50)
    perecible = CharField(max_length=2)
    precio_compra = DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        table_name = 'producto'

class CategoriaProducto(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_delete='CASCADE', on_update='CASCADE')
    id_categoria = ForeignKeyField(column_name='id_categoria', field='id_categoria', model=Categoria, on_delete='CASCADE', on_update='CASCADE')

    class Meta:
        table_name = 'categoria_producto'
        indexes = (
            (('id_categoria', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('id_categoria', 'gtin_producto')

class Proveedor(BaseModel):
    correo_proveedor = CharField(max_length=50, null=True)
    id_direccion = ForeignKeyField(column_name='id_direccion', field='id_direccion', model=Direccion, on_update='CASCADE')
    nombre_proveedor = CharField(max_length=30)
    rut = CharField(max_length=15, primary_key=True)
    telefono_proveedor = CharField(max_length=15, null=True)

    class Meta:
        table_name = 'proveedor'

class Ingresos(BaseModel):
    cantidad_ingreso = IntegerField()
    fecha_ingreso = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_update='CASCADE')
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacen, on_update='CASCADE')
    id_ingresos = AutoField()
    observacion_ingreso = TextField(null=True)
    rut_proveedor = ForeignKeyField(column_name='rut_proveedor', field='rut', model=Proveedor, on_update='CASCADE')

    class Meta:
        table_name = 'ingresos'

class ProductoAlmacen(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_delete='CASCADE', on_update='CASCADE')
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacen, on_delete='CASCADE', on_update='CASCADE')
    stock = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'producto_almacen'
        indexes = (
            (('gtin_producto', 'id_almacen'), True),
        )
        primary_key = CompositeKey('gtin_producto', 'id_almacen')

class ProveedorProducto(BaseModel):
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_delete='CASCADE', on_update='CASCADE')
    rut_proveedor = ForeignKeyField(column_name='rut_proveedor', field='rut', model=Proveedor, on_delete='CASCADE', on_update='CASCADE')

    class Meta:
        table_name = 'proveedor_producto'
        indexes = (
            (('rut_proveedor', 'gtin_producto'), True),
        )
        primary_key = CompositeKey('rut_proveedor', 'gtin_producto')

class Salida(BaseModel):
    cantidad_salida = IntegerField()
    fecha_salida = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    gtin_producto = ForeignKeyField(column_name='gtin_producto', field='gtin', model=Producto, on_update='CASCADE')
    id_almacen = ForeignKeyField(column_name='id_almacen', field='id_almacen', model=Almacen, on_update='CASCADE')
    id_salidas = AutoField()
    motivo_salida = CharField(null=True)

    class Meta:
        table_name = 'salida'

