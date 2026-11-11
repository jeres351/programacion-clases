from negocio.negocio_usuarios import (mostrar_usuarios, crear_objeto_usuario, obtener_usuario,
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
    correo = pedir_correo("Correo: ")
    if existe_usuario(correo):
        print("Ya existe un usuario con ese correo.")
        return

    if existe_usuario_deshabilitado(correo):
        if pedir_si_no("Hay un usuario deshabilitado con ese correo. ¿Quieres habilitarlo de nuevo?"):
            reactivar_usuario(correo)
        else:
            print("Operación cancelada.")
        return

    nombre = pedir_texto("Nombre: ", 25)
    apellido = pedir_texto("Apellido: ", 25)
    contrasena = pedir_contrasena("Contraseña (mínimo 8 caracteres): ")
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