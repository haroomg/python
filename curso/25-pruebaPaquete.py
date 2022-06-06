""" 

paquetes:

directorios (carpetas) donde se almacena modulos relacionados entre si


para que sirve?
para organizar codigo y que no se repita

Como crear un paquete?
crear una carpeta o directorio con un archivo dentro llamado __init__.py

lo que hace __init__.py es "convertir" un directorio en un modulo o paquete 
que contiene otros modulos, y esto lo hace para poder importarlo
"""

from paquete1.funcionesCadena import *
from paquete1.funcionesNumericas import *

print (multiplicar(2,3))
print (potenciar(2,3))
print (contarLetras("hola mundo"))