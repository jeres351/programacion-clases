import re
from datetime import datetime
from decimal import Decimal, InvalidOperation


def pedir_texto(mensaje, max_largo=None, obligatorio=True):
    """Pide un texto. Si no es obligatorio y se deja vacío, devuelve None."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            if obligatorio:
                print("Este campo es obligatorio.")
                continue
            return None
        if max_largo and len(valor) > max_largo:
            print(f"Máximo {max_largo} caracteres.")
            continue
        return valor


def pedir_gtin(mensaje="GTIN del producto: "):
    """Pide el código del producto: letras (A-Z) y números, máximo 14 caracteres."""
    while True:
        gtin = pedir_texto(mensaje, 14)
        if re.fullmatch(r"[A-Za-z0-9]+", gtin):
            return gtin.upper()
        print("El código solo puede contener letras (sin tildes ni ñ) y números, sin espacios ni símbolos.")


def pedir_entero(mensaje, minimo=1, maximo=None):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
        except ValueError:
            print("Debe ingresar un número entero.")
            continue
        if numero < minimo:
            print(f"Debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            print(f"Debe ser menor o igual a {maximo}.")
            continue
        return numero


def pedir_entero_opcional(mensaje, minimo=1):
    """Entero que se puede omitir con Enter (devuelve None)."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            return None
        try:
            numero = int(valor)
        except ValueError:
            print("Debe ingresar un número entero.")
            continue
        if numero < minimo:
            print(f"Debe ser mayor o igual a {minimo}.")
            continue
        return numero


def pedir_decimal(mensaje, minimo=0):
    while True:
        valor = input(mensaje).strip().replace(",", ".")
        try:
            numero = Decimal(valor)
        except InvalidOperation:
            print("Debe ingresar un número (ej: 1990 o 1990.50).")
            continue
        if numero < minimo:
            print(f"Debe ser mayor o igual a {minimo}.")
            continue
        return numero


def pedir_fecha(mensaje, obligatoria=True):
    """Pide una fecha YYYY-MM-DD. Si no es obligatoria, Enter devuelve None."""
    while True:
        valor = input(mensaje).strip()
        if not valor:
            if obligatoria:
                print("Este campo es obligatorio.")
                continue
            return None
        try:
            return datetime.strptime(valor, "%Y-%m-%d").date()
        except ValueError:
            print("Formato inválido. Use YYYY-MM-DD (ej: 2026-12-31).")


def pedir_si_no(mensaje):
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Responda con 's' o 'n'.")
