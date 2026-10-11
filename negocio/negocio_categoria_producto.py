from datos.repositorio.repo_producto import listado_categorias, productos_por_categoria
from prettytable import PrettyTable

def mostrar_categorias_con_productos():
    for cat in listado_categorias():
        print(f"\n=== {cat.nombre_categoria} ===")
        tabla = PrettyTable()
        tabla.field_names = ["GTIN", "Producto", "Precio compra"]
        for p in productos_por_categoria(cat.id_categoria):
            tabla.add_row([p.gtin, p.nombre_producto, p.precio_compra])
        print(tabla)
