from datos.repositorio.repo_proveedor import (listado_proveedores, buscar_proveedor,guardar_proveedor, eliminar_proveedor)
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