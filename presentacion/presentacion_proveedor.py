from negocio.negocio_proveedor import (mostrar_proveedores, crear_objeto_proveedor,
                                       borrar_proveedor, obtener_proveedor,
                                       existe_proveedor_eliminado, reactivar_proveedor)
from auxiliares.entradas import pedir_texto, pedir_si_no
from auxiliares.validacion import validar_rut, validar_correo


def _pedir_rut():
    """Pide el RUT hasta que tenga formato y dígito verificador válidos."""
    while True:
        rut = pedir_texto("RUT del proveedor (ej: 76.123.456-7): ", 15).upper()
        rut_valido, mensaje = validar_rut(rut)
        if rut_valido:
            return rut_valido
        print(mensaje)

def _pedir_correo_opcional():
    """Correo opcional: Enter lo omite; si se escribe, debe tener formato válido."""
    while True:
        correo = pedir_texto("Correo (opcional): ", 50, False)
        if correo is None:
            return None
        correo_valido, mensaje = validar_correo(correo)
        if correo_valido:
            return correo_valido
        print(mensaje)


def ver_proveedores():
    print("\n--- Proveedores ---")
    mostrar_proveedores()

def solicitar_datos_proveedor():
    print("\n--- Agregar proveedor ---")
    rut = _pedir_rut()
    if obtener_proveedor(rut):
        print("Ya existe un proveedor con ese RUT.")
        return

    if existe_proveedor_eliminado(rut):
        if pedir_si_no("Hay un proveedor eliminado con ese RUT. ¿Quieres reactivarlo?"):
            reactivar_proveedor(rut)
        else:
            print("Operación cancelada.")
        return

    nombre_proveedor = pedir_texto("Nombre del proveedor: ", 30)
    correo_proveedor = _pedir_correo_opcional()
    telefono_proveedor = pedir_texto("Teléfono (opcional): ", 15, False)

    print("Dirección del proveedor:")
    calle = pedir_texto("  Calle: ", 100)
    numero_lugar = pedir_texto("  Número: ", 30)
    comuna = pedir_texto("  Comuna: ", 100)
    region = pedir_texto("  Región: ", 100)

    crear_objeto_proveedor(rut, nombre_proveedor, correo_proveedor, telefono_proveedor,
                           calle, numero_lugar, comuna, region)

def solicitar_rut_eliminar():
    print("\n--- Eliminar proveedor ---")
    if not mostrar_proveedores():
        return
    rut = pedir_texto("RUT del proveedor a eliminar: ", 15).upper()
    proveedor = obtener_proveedor(rut)
    if proveedor is None:
        print("No existe un proveedor con ese RUT.")
        return

    if pedir_si_no(f"¿Seguro que quieres eliminar a '{proveedor.nombre_proveedor}'?"):
        borrar_proveedor(rut)
    else:
        print("Operación cancelada.")
