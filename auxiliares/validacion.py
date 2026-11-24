import re

def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron_correo, correo):
        mensaje = 'Formato de correo válido.'
    else:
        mensaje = 'Formato de correo NO corresponde, ingrese nuevamente...'
        correo = ''
    return correo, mensaje


def validar_contrasena(contrasena):
    """Devuelve (es_valida, mensaje). bcrypt solo admite hasta 72 bytes."""
    if len(contrasena) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    if len(contrasena.encode("utf-8")) > 72:
        return False, "La contraseña es demasiado larga (máximo 72 bytes)."
    if not re.search(r"[A-Z]", contrasena):
        return False, "La contraseña debe incluir al menos una letra mayúscula."
    if not re.search(r"[a-z]", contrasena):
        return False, "La contraseña debe incluir al menos una letra minúscula."
    if not re.search(r"\d", contrasena):
        return False, "La contraseña debe incluir al menos un número."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\\[\]]", contrasena):
        return False, "La contraseña debe incluir al menos un símbolo (!@#$%^&*...)."
    return True, "Contraseña válida"

def validar_rut(rut):
    patron_rut = r'^\d{1,3}(?:\.\d{3})*-?[0-9kK]$'

    if re.match(patron_rut, rut):
        rut_limpio = rut.replace('.', '').replace('-', '')
        digito_verificador = rut_limpio[-1]
        numero_rut = rut_limpio[:-1]
        rut_invertido = numero_rut[::-1]

        multiplicador = 2
        suma = []

        for num in rut_invertido:
            multiplicacion = int(num) * multiplicador
            suma.append(multiplicacion)
            multiplicador += 1
            if multiplicador > 7:
                multiplicador = 2

        resto = sum(suma) % 11
        dig_ver_calc = 11 - resto

        if dig_ver_calc == 11:
            dig_ver_calc = '0'
        elif dig_ver_calc == 10:
            dig_ver_calc = 'K'
        else:
            dig_ver_calc = str(dig_ver_calc)

        if digito_verificador == dig_ver_calc:
            mensaje = 'RUT válido'
            return rut, mensaje
        else:
            rut = ''
            mensaje = 'RUT inválido, ingrese nuevamente...'
    else:
        mensaje = 'Formato de RUT NO corresponde, ingrese nuevamente...'
        rut = ''
    return rut, mensaje

def validar_genero(genero):
    if genero not in ['1', '2', '3']:
        mensaje = 'Género Inválido'
        genero = ''
    else:
        mensaje = 'Género Válido'
    return genero, mensaje

class ValidacionError(Exception):
    """Error de validación de reglas de negocio."""
    pass

