from datos.modelos.models import Producto, Categoria, CategoriaProducto

def listado_categorias():
    return Categoria.select()

def productos_por_categoria(id_categoria):
    return (Producto
            .select()
            .join(CategoriaProducto)
            .where(CategoriaProducto.id_categoria == id_categoria))