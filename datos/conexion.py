import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("No se encontró DATABASE_URL en el archivo .env")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def probar_conexion():
    try:
        with engine.connect() as connection:
            print("¡Conexión exitosa a la base de datos en Supabase!")
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    probar_conexion()