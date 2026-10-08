from datos.repositorio.repo_producto import  listado_producto, guardar_producto
from datos.modelos.producto import Producto
from  prettytable import PrettyTable

def lista_productos():
    tabla_producto = PrettyTable()
    tabla_paises.field_names = ['gtin', 'nombre', 'descripcion_producto', 'precio_compra', 'perecible', 'Habilitado']
    paises = listado_paises()
    for pais in paises:
        tabla_paises.add_row([pais.id_pais, pais.pais, pais.nacionalidad, pais.iso2, pais.iso3, ('Deshabilitado','Habilitado')[pais.habilitado]])
    print(tabla_paises)


