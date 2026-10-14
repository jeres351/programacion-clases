from negocio.negocio_categoria_producto import mostrar_categorias, mostrar_productos_de_categoria
from auxiliares.entradas import pedir_entero

def ver_categorias():
    print("\n--- Categorías ---")
    if not mostrar_categorias():
        return
    id_categoria = pedir_entero("Ingrese el ID de la categoría: ")
    mostrar_productos_de_categoria(id_categoria)