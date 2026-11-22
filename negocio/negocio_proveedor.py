from datos.repositorio.repo_proveedor import (listado_proveedores, buscar_proveedor,
                                              buscar_proveedor_eliminado, guardar_proveedor,
                                              eliminar_proveedor, restaurar_proveedor,
                                              asignar_proveedor, producto_tiene_proveedor)
from datos.modelos.models import Proveedor, Direccion
from prettytable import PrettyTable

def mostrar_proveedores():
    proveedores = list(listado_proveedores())
    if not proveedores:
        print("No hay proveedores registrados.")
        return False

    tabla = PrettyTable()
    tabla.field_names = ["RUT", "Proveedor", "Correo", "Teléfono", "Dirección"]
    tabla.align = "l"
    for p in proveedores:
        d = p.id_direccion
        tabla.add_row([p.rut,
                       p.nombre_proveedor,
                       p.correo_proveedor or "-",
                       p.telefono_proveedor or "-",
                       f"{d.calle} {d.numero_lugar}, {d.comuna}, {d.region}"])
    print(tabla)
    return True

def existe_proveedor(rut):
    return buscar_proveedor(rut) is not None

def obtener_proveedor(rut):
    return buscar_proveedor(rut)

def existe_proveedor_eliminado(rut):
    return buscar_proveedor_eliminado(rut) is not None

def reactivar_proveedor(rut):
    return restaurar_proveedor(rut)

def crear_objeto_proveedor(rut, nombre_proveedor, correo_proveedor, telefono_proveedor,
                           calle, numero_lugar, comuna, region):
    nueva_direccion = Direccion()
    nueva_direccion.calle = calle
    nueva_direccion.numero_lugar = numero_lugar
    nueva_direccion.comuna = comuna
    nueva_direccion.region = region

    nuevo_proveedor = Proveedor()
    nuevo_proveedor.rut = rut
    nuevo_proveedor.nombre_proveedor = nombre_proveedor
    nuevo_proveedor.correo_proveedor = correo_proveedor
    nuevo_proveedor.telefono_proveedor = telefono_proveedor
    return guardar_proveedor(nuevo_proveedor, nueva_direccion)

def borrar_proveedor(rut):
    return eliminar_proveedor(rut)

def _normalizar_rut(rut):
    return rut.replace(".", "").replace("-", "").replace(" ", "").upper()

def buscar_rut_proveedor(texto):
    """Devuelve el RUT tal como está guardado, aunque se escriba sin puntos, sin guion
    o en minúscula (ej: 761234567 o 76.123.456-7). Si no hay proveedor activo, devuelve None."""
    buscado = _normalizar_rut(texto)
    for proveedor in listado_proveedores():
        if _normalizar_rut(proveedor.rut) == buscado:
            return proveedor.rut
    return None

def vincular_proveedor_producto(gtin, rut):
    """Asigna un proveedor a un producto existente. Un producto puede tener varios."""
    if producto_tiene_proveedor(gtin, rut):
        print("Ese proveedor ya está asignado a este producto.")
        return False
    return asignar_proveedor(gtin, rut)