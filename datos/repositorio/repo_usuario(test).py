from datos.modelos.models import Usuarios

def listado_usuario():
    try:
        usuarios = usuario.select().where(Usuario.habilitado == True)
        if usuarios:
            return usuarios
    except Exception as e:
        print(f"Ha ocrrudio un error:", (e))

def obetener 