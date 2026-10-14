from negocio.negocio_producto import lista_producto
from negocio.negocio_inventario import mostrar_stock_bajo
from auxiliares.entradas import pedir_entero_opcional

def ver_inventario():
    print("\n--- Inventario ---")
    lista_producto()

def solicitar_stock_bajo():
    print("\n--- Stock bajo ---")
    umbral = pedir_entero_opcional("Umbral de stock (Enter = 100): ", 0)
    if umbral is None:
        umbral = 100
    mostrar_stock_bajo(umbral)