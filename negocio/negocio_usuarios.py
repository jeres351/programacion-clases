from prettytable import PrettyTable
from datos.modelos.models import Usuarios
from datos.repositorio.repo_usuarios import (listado_usuarios_habilitados,
                                             listado_usuarios_deshabilitados,
                                             buscar_usuario,
                                             buscar_usuario_deshabilitado,
                                             buscar_usuario_login,
                                             contar_usuarios_habilitados,
                                             guardar_usuario,
                                             deshabilitar_usuario,
                                             habilitar_usuario)
from auxiliares.seguridad import hashear_contrasena, verificar_contrasena
from auxiliares.validacion import ValidacionError
import re


def mostrar_usuarios(habilitados=True):
    usuarios = list(listado_usuarios_habilitados() if habilitados
                    else listado_usuarios_deshabilitados())
    if not usuarios:
        print("No hay usuarios habilitados." if habilitados else "No hay usuarios deshabilitados.")
        return False

    tabla = PrettyTable()
    tabla.field_names = ["Id", "Nombre completo", "Correo", "Incorporación", "Estado"]
    tabla.align = "l"
    for u in usuarios:
        tabla.add_row([u.id_usuario,
                       f"{u.nombre_usuario} {u.apellido_usuario}",
                       u.correo_usuario,
                       u.fecha_incorporacion,
                       "Habilitado" if u.habilitado else "Deshabilitado"])
    print(tabla)
    return True

def existe_usuario(correo):
    return buscar_usuario(correo) is not None

def obtener_usuario(correo):
    return buscar_usuario(correo)

def existe_usuario_deshabilitado(correo):
    return buscar_usuario_deshabilitado(correo) is not None


def _validar_nombre(valor, campo):
    if not valor or not valor.strip():
        raise ValidacionError(f"El {campo} no puede estar vacío.")
    if re.search(r'\d', valor):
        raise ValidacionError(f"El {campo} no puede contener números.")
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", valor):
        raise ValidacionError(f"El {campo} solo puede contener letras y espacios.")

def crear_objeto_usuario(nombre, apellido, correo, contrasena):

    _validar_nombre(nombre, "nombre")
    _validar_nombre(apellido, "apellido")

    nuevo_usuario = Usuarios()
    nuevo_usuario.nombre_usuario = nombre
    nuevo_usuario.apellido_usuario = apellido
    nuevo_usuario.correo_usuario = correo
    nuevo_usuario.contrasena_usuario = hashear_contrasena(contrasena)   # nunca en texto plano
    return guardar_usuario(nuevo_usuario)

def borrar_usuario(correo):
    # Evita quedarse sin nadie que pueda entrar al sistema cuando exista el login
    if listado_usuarios_habilitados().count() <= 1:
        print("No puedes deshabilitar al último usuario habilitado.")
        return 0
    return deshabilitar_usuario(correo)

def reactivar_usuario(correo):
    return habilitar_usuario(correo)

def hay_usuarios_habilitados():
    return contar_usuarios_habilitados() > 0

def iniciar_sesion(correo, contrasena):
    """Devuelve el usuario si el correo y la contraseña son correctos; si no, None."""
    usuario = buscar_usuario_login(correo)
    if usuario is None:
        return None
    if not verificar_contrasena(contrasena, usuario.contrasena_usuario):
        return None
    return usuario
