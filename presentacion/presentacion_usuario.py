from getpass import getpass
from negocio.negocio_usuarios import (mostrar_usuarios, iniciar_sesion, crear_objeto_usuario, obtener_usuario,
                                      existe_usuario, existe_usuario_deshabilitado,
                                      reactivar_usuario, borrar_usuario)
from auxiliares.entradas import pedir_texto, pedir_correo, pedir_contrasena, pedir_si_no


def ver_usuarios():
    print("\n--- Usuarios habilitados ---")
    mostrar_usuarios(True)

def ver_usuarios_deshabilitados():
    print("\n--- Usuarios deshabilitados ---")
    mostrar_usuarios(False)

def solicitar_datos_usuario():
    print("\n--- Agregar usuario ---")
    nombre = pedir_texto("Nombre: ", 25)
    apellido = pedir_texto("Apellido: ", 25)
    correo = pedir_correo("Correo: ")

    if existe_usuario(correo):
        print("Ya existe un usuario con ese correo.")
        return

    # Si el correo ya pertenece a un usuario deshabilitado,
    # se ofrece reactivarlo en vez de crear uno nuevo.
    if existe_usuario_deshabilitado(correo):
        if pedir_si_no("Hay un usuario deshabilitado con ese correo. ¿Quieres habilitarlo de nuevo?"):
            reactivar_usuario(correo)
        else:
            print("Operación cancelada.")
        return

    contrasena = pedir_contrasena()   # sin eco en pantalla, con confirmación y validación
    crear_objeto_usuario(nombre, apellido, correo, contrasena)


def solicitar_registro():
    """Registro público (antes de iniciar sesión). No reactiva cuentas deshabilitadas."""
    print("\n--- Registrarse ---")
    nombre = pedir_texto("Nombre: ", 25)
    apellido = pedir_texto("Apellido: ", 25)
    correo = pedir_correo("Correo: ")

    if existe_usuario(correo) or existe_usuario_deshabilitado(correo):
        print("No se puede registrar con ese correo.")
        return

    contrasena = pedir_contrasena()
    crear_objeto_usuario(nombre, apellido, correo, contrasena)


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


def solicitar_login(max_intentos=3):
    """Pide correo y contraseña. Devuelve el usuario si entra, o None tras agotar los intentos."""
    print("\n--- Iniciar sesión ---")
    for intento in range(1, max_intentos + 1):
        correo = pedir_texto("Correo: ", 255)
        contrasena = getpass("Contraseña: ")
        usuario = iniciar_sesion(correo, contrasena)
        if usuario is not None:
            print(f"Bienvenido/a, {usuario.nombre_usuario} {usuario.apellido_usuario}.")
            return usuario
        print(f"Correo o contraseña incorrectos. Intento {intento} de {max_intentos}.")
    print("Demasiados intentos fallidos.")
    return None
