from decouple import config
from peewee import MySQLDatabase

def crear_conexion():
    db = MySQLDatabase(config('DB_NAME'), **{
        'charset': 'utf8mb4',
        'host': config('DB_HOST'),
        'port': config('DB_PORT', cast=int),
        'user': config('DB_USER'),
        'password': config('DB_PASSWORD')
    })
    return db