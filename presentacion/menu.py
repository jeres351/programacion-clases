import sys
from auxiliares.opciones_menu import menu_superior

def menu_principal():
    print('Biblio-Hub')
    print('==========\n')

    while True:
        for clave,valor in menu_superior.items():
            print(f'[{clave}] - {valor}')

        opcion_usuario = input(f'Ingrese su opción [0-{len(menu_superior)-1}]')
        if opcion_usuario == '1':
            print('Seleccionada la opción 1.\n')
        elif opcion_usuario == '2':
            print('Seleccionada la opción 2.\n')
        elif opcion_usuario == '3':
            print('Seleccionada la opción 3.\n')
        elif opcion_usuario == '0':
            print('Saliendo...')
            sys.exit()
        else:
            print('Opción seleccionada NO corresponde...\nIntente nuevamente...\n')