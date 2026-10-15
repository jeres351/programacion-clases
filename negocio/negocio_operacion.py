from datos.repositorio.repo_operacion import (listado_almacenes, buscar_almacen, stock_disponible,
                                              registrar_ingreso, registrar_salida,
                                              historial_ingresos, historial_salidas)
from prettytable import PrettyTable

def mostrar_almacenes():
    almacenes = list(listado_almacenes())
    if not almacenes:
        print("No hay almacenes registrados.")
        return False

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Almacén", "Dirección"]
    tabla.align = "l"
    for a in almacenes:
        d = a.id_direccion
        tabla.add_row([a.id_almacen, a.nombre_almacen, f"{d.calle} {d.numero_lugar}, {d.comuna}"])
    print(tabla)
    return True

def existe_almacen(id_almacen):
    return buscar_almacen(id_almacen) is not None

def obtener_stock(gtin, id_almacen):
    return stock_disponible(gtin, id_almacen)

def registrar_entrada(gtin, id_almacen, rut_proveedor, cantidad, observacion):
    return registrar_ingreso(gtin, id_almacen, rut_proveedor, cantidad, observacion)

def registrar_salida_producto(gtin, id_almacen, cantidad, motivo):
    return registrar_salida(gtin, id_almacen, cantidad, motivo)

def mostrar_historial(gtin=None, limite=30):
    movimientos = []

    for fecha, g, nombre, almacen, cantidad, proveedor, obs in historial_ingresos(gtin):
        detalle = f"Proveedor: {proveedor}" + (f" | {obs}" if obs else "")
        movimientos.append((fecha, "ENTRADA", g, nombre, almacen, f"+{cantidad}", detalle))

    for fecha, g, nombre, almacen, cantidad, motivo in historial_salidas(gtin):
        movimientos.append((fecha, "SALIDA", g, nombre, almacen, f"-{cantidad}", motivo or "-"))

    if not movimientos:
        print("No hay movimientos registrados.")
        return

    movimientos.sort(key=lambda m: str(m[0]), reverse=True)

    tabla = PrettyTable()
    tabla.field_names = ["Fecha", "Tipo", "GTIN", "Producto", "Almacén", "Cantidad", "Detalle"]
    tabla.align = "l"
    for m in movimientos[:limite]:
        tabla.add_row(m)
    print(tabla)
    if len(movimientos) > limite:
        print(f"Mostrando los últimos {limite} de {len(movimientos)} movimientos.")