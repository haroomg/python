# sets - son colecciones desordenadas de objetos unicos

from ctypes.wintypes import PINT


canasta = {'manzana', 'pera', 'platano', 'naranja', 'manzana', 'pera'}
print(canasta)

numeros = {1,2,3,4,5,1,2,3,4,5}
print(numeros)


# Tipo 1 de sets: Set mutables
a = set('abracadabra') # mutables, se pueden agregar nuevos elementos
print(a)

a.add("g")
print(a)

a.add('a')
print(a) # no se agrega el elemento ya que es unico

# Tipo 2 de sets: Set inmutables (frozen set) no se pueden agregar nuevos elementos

b = frozenset('perro')
print(b)

# b.app('t') # dara error ya que no se pueden agragr nuevos alementos a un set inmutable

# intersection - devuelve un set con los elementos que estan en ambos sets
miSet = {1,2,3,4,5}.intersection({1,2,3,4,5,6,7,8,9,10})
print(miSet)

miSet2 = {1,2,6,9,8} & miSet
print(miSet2)


# union - permite la union de dos sets,agreagndo los elementos que no estan duplicados
miSetEjemplo = {"casa",1,2,3,4,5,6}

miSet3 = {1,2,3,4,5}.union(miSetEjemplo)
print(miSet3)

miSet3 = {"casa",1,2,3,"perro","gato"} | miSetEjemplo
print(miSet3)


# difference - Devuelve los elementos que son diferentes del primer set al segundo
miSet4 = {1,2,3,4,5}.difference({1,2,6,7,8,9,10})
print(miSet4)

miSet4 = {1,2,3,4,5} - {1,2,5}
print(miSet4)


# symmetric difference - devuelve los elementos que no se encuentras en un set con respecto a otro y viseversa
miSet5 = {1,2,3,4}.symmetric_difference({2,3,5})
print(miSet5)

# issuperset - devuelve True si el set es un superset del otro
# issubset - devuelve True si el set es un subset del otro

miSet6 = {1,2,3,4,5}.issuperset({1,2,3})
print(miSet6)

miSet7 = {1,2,3,4,5}.issubset({1,2,3})
print(miSet7)