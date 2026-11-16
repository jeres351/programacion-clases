from negocio.negocio_usuarios import (mostrar_usuarios, crear_objeto_usuario, obtener_usuario,
                                      existe_usuario, existe_usuario_deshabilitado,
                                      reactivar_usuario, borrar_usuario)
from auxiliares.entradas import pedir_texto, pedir_correo, pedir_contrasena, pedir_si_no
from auxiliares.validacion import validar_rut,validar_correo,validar_genero


def ver_usuarios():
    print("\n--- Usuarios habilitados ---")
    mostrar_usuarios(True)

def ver_usuarios_deshabilitados():
    print("\n--- Usuarios deshabilitados ---")
    mostrar_usuarios(False)

def solicitar_datos_usuario():
    print("\n--- Agregar usuario ---")
    try:
        rut = nombre = apellido = correo = pais = fecha_nacimiento = genero = contrasena = ''

        print('Ingrese Datos de Usuario')
        print('========================')

        while rut == '':
            rut = input('\nRUT (12.345.678-9): ').strip()
            rut, mensaje = validar_rut(rut)
            print(mensaje)

        while nombre == '':
            nombre = input('\nNombre: ').strip()

        while apellido == '':
            apellido = input('\nApellido: ').strip()

        while correo == '':
            correo = input('\nCorreo: ').strip()
            correo, mensaje = validar_correo(correo)
            print(mensaje)

        # Si el correo ya pertenece a un usuario deshabilitado,
        # se ofrece reactivarlo en vez de crear uno nuevo.
        if existe_usuario_deshabilitado(correo):
            if pedir_si_no("Hay un usuario deshabilitado con ese correo. ¿Quieres habilitarlo de nuevo?"):
                reactivar_usuario(correo)
            else:
                print("Operación cancelada.")
            return None

        while pais == '':
            pais = input('\nNacionalidad: ').strip()

        while fecha_nacimiento == '':
            fecha_nacimiento = input('\nFecha Nacimiento: ').strip()

        while genero == '':
            print('Seleccione Género')
            print('[1] Masculino')
            print('[2] Femenino')
            print('[3] Otro')
            genero = input('\nGénero: ').strip()
            genero, mensaje = validar_genero(genero)
            print(mensaje)

        while contrasena == '':
            contrasena = input('\nContraseña: ').strip()

        return rut, nombre, apellido, correo, pais, fecha_nacimiento, genero, contrasena

    except Exception as error:
        print(f'Error al solicitar los datos del usuario: {error}')
        return None


def solicitar_correo_deshabilitar():
    print("\n--- Deshabilitar usuario ---")
    if not mostrar_usuarios(True):
        return
    correo = pedir_correo("Correo del usuario a deshabilitar: ")
    usuario = obtener_usuario(correo)
    if usuario is None:
        print("No existe un usuario habilitado con ese correo.")
        return

    if pedir_si_no(f"¿Seguro que quieres deshabilitar a '{usuario.nombre_usuario} {usuario.apellido_usuario}'?"):
        borrar_usuario(correo)
    else:
        print("Operación cancelada.")