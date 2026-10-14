from negocio.negocio_producto import crear_objeto_producto, borrar_producto, obtener_producto, lista_producto
from negocio.negocio_categoria_producto import mostrar_categorias, existe_categoria
from negocio.negocio_proveedor import mostrar_proveedores, existe_proveedor
from auxiliares.entradas import (pedir_texto, pedir_gtin, pedir_decimal, pedir_fecha,pedir_si_no, pedir_entero_opcional)

def solicitar_datos_producto():
    print("\n--- Agregar producto ---")
    gtin = pedir_gtin("Ingrese el GTIN del producto: ")
    if obtener_producto(gtin):
        print("Ya existe un producto con ese GTIN.")
        return

    nombre_producto = pedir_texto("Ingrese el nombre del producto: ", 50)
    descripcion_producto = pedir_texto("Ingrese la descripción del producto (opcional): ", None, False)
    precio_compra = pedir_decimal("Ingrese el precio de compra del producto: ")
    perecible = "SI" if pedir_si_no("¿El producto es perecible?") else "NO"
    fecha_vencimiento = None
    if perecible == "SI":
        fecha_vencimiento = pedir_fecha("Fecha de vencimiento (YYYY-MM-DD): ")

    id_categoria = None
    if mostrar_categorias():
        id_categoria = pedir_entero_opcional("ID de la categoría (Enter para omitir): ")
        if id_categoria is not None and not existe_categoria(id_categoria):
            print("No existe esa categoría, se omite.")
            id_categoria = None

    rut_proveedor = None
    if mostrar_proveedores():
        rut_proveedor = pedir_texto("RUT del proveedor (Enter para omitir): ", 15, False)
        if rut_proveedor and not existe_proveedor(rut_proveedor):
            print("No existe ese proveedor, se omite.")
            rut_proveedor = None

    crear_objeto_producto(gtin, nombre_producto, descripcion_producto, precio_compra, perecible,fecha_vencimiento, id_categoria, rut_proveedor)

def solicitar_gtin_eliminar():
    print("\n--- Eliminar producto ---")
    lista_producto()
    gtin = pedir_gtin("Ingrese el GTIN del producto a eliminar: ")
    producto = obtener_producto(gtin)
    if producto is None:
        print("No existe un producto con ese GTIN.")
        return

    if pedir_si_no(f"¿Seguro que quieres eliminar '{producto.nombre_producto}'?"):
        borrar_producto(gtin)
    else:
        print("Operación cancelada.")
