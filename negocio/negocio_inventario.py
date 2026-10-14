from datos.repositorio.repo_inventario import stock_bajo
from prettytable import PrettyTable

def mostrar_stock_bajo(umbral):
    filas = list(stock_bajo(umbral))
    if not filas:
        print(f"No hay productos con stock menor o igual a {umbral}.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["GTIN", "Producto", "Almacén", "Stock"]
    tabla.align = "l"
    for gtin, nombre, almacen, stock in filas:
        tabla.add_row([gtin, nombre, almacen or "Sin stock registrado", stock if stock is not None else 0])
    print(tabla)