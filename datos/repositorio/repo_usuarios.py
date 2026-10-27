from datos.modelos.models import Usuarios
from peewee import IntegrityError, OperationalError, PeeweeException
 
def listado_usuarios():
    return Usuarios.select().order_by(Usuarios.correo_usuario)
 
def buscar_usuario(correo):
    return Usuarios.get_or_none(Usuarios.correo_usuario == correo)
 
def guardar_usuario(usuario):
    try:
        usuario_guardado = usuario.save(force_insert=True)
        if usuario_guardado == 1:
            print("Usuario guardado correctamente. correo del usuario:", usuario.correo_usuario)
            return True
    except IntegrityError as e:
        print(f"Error de clave única (¿el correo ya existe?): {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
    return False
 
def eliminar_usuario(correo):
    try:
        filas = Usuarios.delete().where(Usuarios.correo_usuario == correo).execute()
        if filas == 1:
            print("Usuario eliminado correctamente.")
        else:
            print("No existe un usuario con ese correo.")
        return filas
    except IntegrityError as e:
        print(f"No se puede eliminar, el usuario está referenciado en otra tabla: {e}")
    except OperationalError as e:
        print(f"Se ha perdido la conexión con el servidor DB: {e}")
    except PeeweeException as e:
        print(f"Ha ocurrido un error genérico: {e}")
 