"""
modulos:
es un archivo con extencion .py o .pyc (Python conpilado), que posee su propio espacio de nombres
y que puede contener variables, funciones, clases o incluso otros modulos.

para que sirve?
para organizar mejor el codigo y poder reutilizarlo mejor.
modulacion y reutilizacion de codigo
"""

import funcionesMatematicas as fm # ya que el nombre del archivo es demasiado largo lo podemos abreviar a fm
print (fm.sumar(1,2))
print (fm.multiplicar(1,2))

from funcionesMatematicas import sumar, multiplicar # podemos importar todas las funciones que queramos llamando cad una o podemos llamar todad de una ves usando *

print (sumar(10,10))
print (multiplicar(10,10))
