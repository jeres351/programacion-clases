from negocio.negocio_producto import crear_objeto_producto

def solicitar_datos_producto():
    gtin = input("Ingrese el GTIN del producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    descripcion_producto = input("Ingrese la descripción del producto: ")
    precio_compra = float(input("Ingrese el precio de compra del producto: "))
    perecible = "SI" if input("¿El producto es perecible? (s/n): ").lower() == "s" else "NO"
    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD, vacío si no aplica): ") or None    

    crear_objeto_producto(gtin, nombre_producto, descripcion_producto, precio_compra, perecible, fecha_vencimiento)