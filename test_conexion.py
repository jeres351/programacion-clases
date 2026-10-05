from datos.conexion import crear_conexion

db = crear_conexion()

try:
    db.connect()
    print("Conexión exitosa")

    # Consulta simple para confirmar que el servidor responde
    cursor = db.execute_sql("SELECT 1")
    print("Respuesta del servidor:", cursor.fetchone())

    # Lista las tablas que existen en la base
    print("Tablas encontradas:", db.get_tables())
except Exception as e:
    print("Error de conexión:", e)
finally:
    if not db.is_closed():
        db.close()