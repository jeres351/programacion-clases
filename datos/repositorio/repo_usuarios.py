from datos.modelos.models import Usuarios
from peewee import IntegrityError, OperationalError, PeeweeException


def listado_usuarios_habilitados():
    return (Usuarios.select()
            .where(Usuarios.habilitado == True)
            .order_by(Usuarios.id_usuario))

def listado_usuarios_deshabilitados():
    return (Usuarios.select()
            .where(Usuarios.habilitado == False)
            .order_by(Usuarios.id_usuario))

def buscar_usuario(correo):
    """Solo usuarios habilitados."""
    return Usuarios.get_or_none((Usuarios.correo_usuario == correo) &
                                (Usuarios.habilitado == True))

def buscar_usuario_deshabilitado(correo):
    return Usuarios.get_or_none((Usuarios.correo_usuario == correo) &
                                (Usuarios.habilitado == False))

def guardar_usuario(usuario):
    try:
        usuario.save()
        print(f"Usuario guardado correctamente. Id: {usuario.id_usuario}")
        return True
    except IntegrityError as e:
        print(f"Error de clave única (¿el correo ya existe?): {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    return False

def deshabilitar_usuario(correo):
    try:
        filas = (Usuarios
                 .update(habilitado=False)
                 .where((Usuarios.correo_usuario == correo) & (Usuarios.habilitado == True))
                 .execute())
        if filas == 1:
            print("Usuario deshabilitado correctamente.")
        else:
            print("No existe un usuario habilitado con ese correo.")
        return filas
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")

def habilitar_usuario(correo):
    try:
        filas = (Usuarios
                 .update(habilitado=True)
                 .where((Usuarios.correo_usuario == correo) & (Usuarios.habilitado == False))
                 .execute())
        if filas == 1:
            print("Usuario habilitado nuevamente.")
        return filas
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")