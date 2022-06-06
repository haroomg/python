# Generadores: permite extraer valores de una funcion y almacenarlos 
# (de uno en uno ) en objetos iterables (que se pueden recorrer)
# sin la necesidad de almacenar todos a la vez en la memoria RAM

# sin usar los genradores
def generaMultiplos(limite):
    numero = 1
    listaNumero = []

    while numero <= limite:
        listaNumero.append(numero * 7)
        numero += 1

    return listaNumero # retornamos toda la lista 

print(generaMultiplos(10))


# usando los generadores - yield
def generaMultiplos2(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7 # ceder la instruccion "yield" genera un objeto iterable
        numero += 1
        
obtineMultiplos = generaMultiplos2(10)

# next(): retorna el siguiente valor del objeto iterable

print(next(obtineMultiplos))
print(next(obtineMultiplos))
print(next(obtineMultiplos))

# son mas eficiantes que las funciones tradicionales
#muy utiles con listas de valores infinitos
# entre llamada y llamada, el objeto iterable entra en un estado de espera