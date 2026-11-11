import re


def validar_correo(correo):
    """Devuelve (correo_normalizado, mensaje). Si es inválido, el correo vuelve vacío."""
    correo = correo.strip().lower()
    if len(correo) <= 255 and re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", correo):
        return correo, "Correo válido"
    return "", "Correo inválido (ej: nombre@dominio.cl)"


def validar_contrasena(contrasena):
    """Devuelve (es_valida, mensaje). bcrypt solo admite hasta 72 bytes."""
    if len(contrasena) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    if len(contrasena.encode("utf-8")) > 72:
        return False, "La contraseña es demasiado larga (máximo 72 bytes)."
    return True, "Contraseña válida"