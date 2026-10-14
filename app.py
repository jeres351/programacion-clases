from presentacion.menu import menu_principal
from datos.modelos.models import BaseModel

if __name__ == '__main__':
    try:
        menu_principal()
    except (KeyboardInterrupt, EOFError):
        print('\nSaliendo...')
    finally:
        db = BaseModel._meta.database
        if not db.is_closed():
            db.close()