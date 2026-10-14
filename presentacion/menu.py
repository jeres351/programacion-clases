from unittest import case

from peewee import PeeweeException
from auxiliares.opciones_menu import (menu_superior, menu_inventario, menu_operaciones,menu_productos, menu_proveedores)
from presentacion.presentacion_inventario import ver_inventario, solicitar_stock_bajo
from presentacion.presentacion_categoria_producto import ver_categorias
from presentacion.presentacion_operacion import (solicitar_datos_entrada, solicitar_datos_salida,solicitar_historial)
from presentacion.presentacion_producto import solicitar_datos_producto, solicitar_gtin_eliminar
from presentacion.presentacion_proveedor import (ver_proveedores, solicitar_datos_proveedor,solicitar_rut_eliminar)


def _pedir_opcion(titulo, opciones):
    print(f'\n{titulo}')
    print('-' * len(titulo))
    for clave, valor in opciones.items():
        print(f'[{clave}] - {valor}')
    return input(f'Ingrese su opción [0-{len(opciones)-1}]: ').strip()


def _ejecutar(accion):
    try:
        accion()
    except PeeweeException as e:
        print(f'Error de base de datos: {e}')


def _submenu(titulo, opciones, acciones):
    while True:
        opcion_usuario = _pedir_opcion(titulo, opciones)
        if opcion_usuario == '0':
            return
        accion = acciones.get(opcion_usuario)
        if accion is None:
            print('Opción seleccionada NO corresponde...\nIntente nuevamente...')
            continue
        _ejecutar(accion)


def menu_inventario_opciones():
    _submenu('Inventario', menu_inventario, {
        '1': ver_inventario,
        '2': ver_categorias,
        '3': solicitar_stock_bajo,
    })


def menu_operaciones_opciones():
    _submenu('Operaciones', menu_operaciones, {
        '1': solicitar_datos_entrada,
        '2': solicitar_datos_salida,
        '3': solicitar_historial,
    })


def menu_productos_opciones():
    _submenu('Productos', menu_productos, {
        '1': solicitar_datos_producto,
        '2': solicitar_gtin_eliminar,
    })


def menu_proveedores_opciones():
    _submenu('Proveedores', menu_proveedores, {
        '1': ver_proveedores,
        '2': solicitar_datos_proveedor,
        '3': solicitar_rut_eliminar
    })


def menu_principal():
    print('Inventario PYME')
    print('===============')

    while True:
        opcion_usuario = _pedir_opcion('Menú principal', menu_superior)
        match opcion_usuario:
            case '1':
                menu_inventario_opciones()
            case '2':
                menu_operaciones_opciones()
            case '3':
                menu_productos_opciones()
            case '4':
                menu_proveedores_opciones()
            case '0':
                print('Saliendo...')
                return
            case _:
                print('Opción seleccionada NO corresponde...\nIntente nuevamente...')
           