"""
Tuplas:  es una estructura de datos propia que permite almacenar distintos tipos de datos
son inmutables: no cambian su valor una vez se han creado
"""
tupla = (1,2,3,4,5,6,7,8,9,10,1)
print(tupla)

tupla2 = ('a','b','c','d','e','f','g','h','i','j')
print(tupla2)

tupla3 = ("hola", 25, 25.2, 56 + 6j, True)
print(tupla3)

tupla4 = (
    (1,2,3,4,5,6,7,8,9,10),
    ("a","b","c","d","e","f","g","h","i","j"),
    ("hola", 25, 25.2, 56 + 6j, True)
)
print(tupla4)

#para consultar un elemento de una tupla 
print(tupla2[0])

#para acceder al ultimo elemento de una tupla
print(tupla2[-1])
print(tupla4[-2])

# desectruturacion de tuplas
a, b, c = tupla4
print(a)
print(b)
print(c)


# count - nos dice cunatas veces se repite un elemento en la tupla
print (tupla.count(1))

# index - nos dice si un elemento esta en la tupla y nos devuelve su posicion
print(tupla.index(1,1))