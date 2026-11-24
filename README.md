Este es nuestro proyecto de POO (Programacion Orientada a Objetos). En el que hicimos un inventario para una PYME.

integrantes_:
Jorge_Ortiz_Castillo
Elizabet__cañete
jeremias_jesus_federico_alonzo_reyes_:muños

Descripcion general: 
En este proyecto se realizo el paso a paso para poder tener una plantilla base para un inventario para una pyme. Teniendo tanto:
Datos de Almacen, Categoria de Productos, Direccion, Ingresos, Productos en almacen, Productos en general, Proveedores, Los productos de 
esos proovedores, El registro de Salidas y entradas, Y por ultimo Registro de Usuarios.

Dependencias:
bcrypt==5.0.0
cffi==2.1.1
cryptography==50.0.2
peewee==4.5.2
prettytable==3.18.0
pycparser==3.1
PyMySQL==1.2.3
python-decouple==3.8

Procedimiento de Instalacion:
en la terminal poner estos comandos

py -m venv .venv

.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt

Procedimiento de Base de Datos:

Ir a la carpeta SQL en Datos. 
Copiar y Pegar el contenido de Inventario.SQL

Usuario inicial:

Ir a la Carpeta SQL en Datos
Copiar y pega el contenido de Usuario.SQL
(asignar de manera manual nombre)


Procedimiento de Ejecucion:

Una vez instalado dependencias, Insertado Bases de datos y Creado usuario en la Base de datos SQL.
Procede con el archivo APP.PY y ejecutarlo ya sea en Terminal U Similar.

