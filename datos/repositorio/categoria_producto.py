from datos.modelos.models import Producto, Categoria, CategoriaProducto
from peewee import IntegrityError, OperationalError, PeeweeException

def listado_categorias():
    return Categoria.select().order_by(Categoria.id_categoria)

def buscar_categoria_por_id(id_categoria):
    return Categoria.get_or_none(Categoria.id_categoria == id_categoria)

def productos_por_categoria(id_categoria):
    return (Producto
            .select()
            .join(CategoriaProducto)
            .where(CategoriaProducto.id_categoria == id_categoria))

def asignar_categoria(gtin, id_categoria):
    try:
        CategoriaProducto.create(gtin_producto=gtin, id_categoria=id_categoria)
        print("Categoría asignada al producto.")
        return True
    except IntegrityError as e:
        print(f"No se pudo asignar la categoría: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    return False