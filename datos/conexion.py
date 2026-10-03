from decouple import config
from peewee import MySQLDatabase, PostgresqlDatabase, SqliteDatabase

def crear_conexion():
    motor = config("DB_ENGINE", default="sqlite").lower()

    if motor == "sqlite":
        return SqliteDatabase(config("DB_NAME", default="app.db"))

    motores = {
        "mysql": (MySQLDatabase, 3306),
        "postgres": (PostgresqlDatabase, 5432),
    }
    if motor not in motores:
        raise ValueError(f"Motor no soportado: {motor}")

    clase, puerto = motores[motor]
    return clase(
        config("DB_NAME"),
        user=config("DB_USER"),
        password=config("DB_PASSWORD"),
        host=config("DB_HOST", default="localhost"),
        port=config("DB_PORT", default=puerto, cast=int),
    )