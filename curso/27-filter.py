# funciones de orden superior (programacion funcional)

# verificar que los elementos de una lista cumplan una determinada condicion
# devolviendo un objeto iterable (iterador) con los elementos que cumplieron ese condicion

from logging import Filterer


edades = [11, 12, 14, 18, 10, 17, 6, 99]

def mayorEdad (edad):
    
    if edad >= 18:
        return True
    
#print(filter(mayorEdad, edades))

edadesMyoresEdad = list (filter(mayorEdad, edades))

print(edadesMyoresEdad)