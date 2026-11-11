import bcrypt


def hashear_contrasena(contrasena):
    """Devuelve el hash bcrypt (60 caracteres) listo para guardar en la BD."""
    return bcrypt.hashpw(contrasena.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_contrasena(contrasena, hash_guardado):
    """True si la contraseña coincide con el hash guardado (se usará en el login)."""
    try:
        return bcrypt.checkpw(contrasena.encode("utf-8"), hash_guardado.encode("utf-8"))
    except ValueError:
        return False