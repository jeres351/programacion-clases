from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Numeric,
    SmallInteger,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from .conexion import Base


class Direccion(Base):
    __tablename__ = 'direccion'

    id_direccion = Column(Integer, primary_key=True, autoincrement=True)
    numero_lugar = Column(String(30), nullable=False)
    calle = Column(String(100), nullable=False)
    comuna = Column(String(100), nullable=False)
    region = Column(String(100), nullable=False)

    proveedores = relationship("Proveedor", back_populates="direccion")
    almacenes = relationship("Almacen", back_populates="direccion")


class Proveedor(Base):
    __tablename__ = 'proveedor'

    rut = Column(String(15), primary_key=True)
    nombre = Column(String(30))
    correo = Column(String(50))
    id_direccion = Column(Integer, ForeignKey('direccion.id_direccion'), nullable=False)

    direccion = relationship("Direccion", back_populates="proveedores")
    ingresos = relationship("Ingresos", back_populates="proveedor")
    productos = relationship("ProveedorProducto", back_populates="proveedor")


class Categoria(Base):
    __tablename__ = 'categoria'

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(35), nullable=False)
    descripcion_categoria = Column(Text, nullable=True)

    productos = relationship("CategoriaProducto", back_populates="categoria")


class Producto(Base):
    __tablename__ = 'producto'

    gtin = Column(String(14), primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion_producto = Column(Text, nullable=True)
    precio_compra = Column(Numeric(10, 2))
    perecible = Column(SmallInteger, default=0)

    ingresos = relationship("Ingresos", back_populates="producto")
    salidas = relationship("Salida", back_populates="producto")
    proveedores = relationship("ProveedorProducto", back_populates="producto")
    categorias = relationship("CategoriaProducto", back_populates="producto")
    almacenes = relationship("ProductoAlmacen", back_populates="producto")


class Almacen(Base):
    __tablename__ = 'almacen'

    id_almacen = Column(Integer, primary_key=True, autoincrement=True)
    nombre_almacen = Column(String(50))
    id_direccion = Column(Integer, ForeignKey('direccion.id_direccion'), nullable=False)

    direccion = relationship("Direccion", back_populates="almacenes")
    productos = relationship("ProductoAlmacen", back_populates="almacen")


class Ingresos(Base):
    __tablename__ = 'ingresos'

    id_ingresos = Column(Integer, primary_key=True, autoincrement=True)
    gtin_producto = Column(String(14), ForeignKey('producto.gtin'))
    fecha_ingreso = Column(DateTime, default=datetime.now)
    cantidad = Column(Integer, nullable=False)
    observacion = Column(Text)
    rut_proveedor = Column(String(15), ForeignKey('proveedor.rut'))

    producto = relationship("Producto", back_populates="ingresos")
    proveedor = relationship("Proveedor", back_populates="ingresos")


class Salida(Base):
    __tablename__ = 'salida'

    id_salidas = Column(Integer, primary_key=True, autoincrement=True)
    gtin_producto = Column(String(14), ForeignKey('producto.gtin'))
    cantidad = Column(Integer, nullable=False)
    fecha_salida = Column(DateTime, default=datetime.now)
    motivo = Column(String(255))

    producto = relationship("Producto", back_populates="salidas")


# --- Tablas Intermedias ---

class ProveedorProducto(Base):
    __tablename__ = 'proveedor_producto'

    rut_proveedor = Column(String(15), ForeignKey('proveedor.rut'), primary_key=True)
    gtin_producto = Column(String(14), ForeignKey('producto.gtin'), primary_key=True)

    proveedor = relationship("Proveedor", back_populates="productos")
    producto = relationship("Producto", back_populates="proveedores")


class CategoriaProducto(Base):
    __tablename__ = 'categoria_producto'

    id_categoria = Column(Integer, ForeignKey('categoria.id_categoria'), primary_key=True)
    gtin_producto = Column(String(14), ForeignKey('producto.gtin'), primary_key=True)

    categoria = relationship("Categoria", back_populates="productos")
    producto = relationship("Producto", back_populates="categorias")


class ProductoAlmacen(Base):
    __tablename__ = 'producto_almacen'

    gtin_producto = Column(String(14), ForeignKey('producto.gtin'), primary_key=True)
    id_almacen = Column(Integer, ForeignKey('almacen.id_almacen'), primary_key=True)
    stock = Column(Integer, nullable=False)

    producto = relationship("Producto", back_populates="almacenes")
    almacen = relationship("Almacen", back_populates="productos")