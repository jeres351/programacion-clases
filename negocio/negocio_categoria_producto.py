from datos.repositorio.categoria_producto import (listado_categorias, buscar_categoria_por_id,
                                                  productos_por_categoria)
from prettytable import PrettyTable

def mostrar_categorias():
    categorias = list(listado_categorias())
    if not categorias:
        print("No hay categorías registradas.")
        return False

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Categoría", "Descripción"]
    tabla.align = "l"
    for c in categorias:
        tabla.add_row([c.id_categoria, c.nombre_categoria, c.descripcion_categoria or "-"])
    print(tabla)
    return True

def existe_categoria(id_categoria):
    return buscar_categoria_por_id(id_categoria) is not None

def mostrar_productos_de_categoria(id_categoria):
    cat = buscar_categoria_por_id(id_categoria)
    if cat is None:
        print("No existe una categoría con ese ID.")
        return

    print(f"\n=== {cat.nombre_categoria} ===")
    productos = list(productos_por_categoria(id_categoria))
    if not productos:
        print("Esta categoría no tiene productos.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["GTIN", "Producto", "Precio compra"]
    tabla.align = "l"
    for p in productos:
        tabla.add_row([p.gtin, p.nombre_producto, p.precio_compra])
    print(tabla)