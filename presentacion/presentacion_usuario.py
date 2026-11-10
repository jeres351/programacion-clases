
from auxiliares.validacion import validar_correo




from sys import exception


def solicitar_datos_usuario():
    try:
        correo_usuario = contrasena_usuario = ''


        while correo_usuario == '':
            correo_usuario = input("Ingrese el correo del usuario: ")
            correo_usuario, mensaje = validar_correo(correo_usuario)

        while contrasena_usuario == '':
            contrasena_usuario = input("Ingrese la contraseña del usuario: ")
       

        return(correo_usuario, contrasena_usuario)
    except exception as e:
        print(f"Mensaje de error: {e}")



def agregar_usuario():
    try:
        correo_usuario, contrasena_usuario = solicitar_datos_usuario()