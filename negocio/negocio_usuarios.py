from prettytable import PrettyTable

from datetime import datetime
import re

from datos.modelos.models import Usuarios
from datos.repositorio.repo_usuarios import listado_usuarios, buscar_usuario, guardar_usuario, eliminar_usuario





def crear_objeto_usuario(tabla: PrettyTable):
    
    