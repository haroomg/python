# listas: son estructuras de datos propias que permite almacenar distintos tipos de datos.
# son equivalestes a los arrays en otro lenguaje de programacion
# son estruturas de datos que pueden mutar

lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista3 = [True, False]
lista4 = ["hello word", 25, 2.32, 56 + 6j, True]

print(lista)
print(lista2[:]) # nos devuelve toda la lista
print(lista3[0]) #nos devuelve un elemento de la lista
print(lista4[-1]) # de esta forma se puedes acceder al ultimo elemento de una lista
print(lista4[0:3]) # nos devuelve una lista desde el elemento 0 hasta el elemento 3
print(lista4[:2]) # nos devuelve una lista desde el elemento 0 hasta el elemento 2
print(lista4[2:]) # nos devuelve una lista desde el elemento 2 hasta el final

lista4.append("nuevo elemento de prueba") #agrega un nuevo lemento a la lista, pero lo agrega al final.
print(lista4)

lista4.insert(0, "primer elemento") # agrega un nuevo elemento a la lista en la posicion que nosotros seleccionamos
print(lista4)

lista.extend(lista2) # agrega una lista a otra
print(lista)

print(lista.index(1)) # nos devuelve la posicion del elemento que nosotros le pasamos

lista4.remove("primer elemento") # elemina el elemento que nosotros le pasamos
print(lista4)

lista4.pop() # elimina el ultimo elemento de la lista
print(lista4)

print(len(lista4)) # nos devuelve la longitud de la lista

# sumar dos listas
lista5 = [1,2,3,4,5,6,7,8,9,10]
lista6 = ["numeros del uno al diez"]
listaSumada = lista5 + lista6
print(listaSumada)

# tambien podemos hacer que los elementos de una lista se repitan cuantas veces queramos
print(lista5 * 3)
lista5.insert(0, "estamos averiguando si este valor esta en la lista")
print(lista5 )

# para comporbar si un elemento esta en la lista, el cual si esta o no nos un valor booleano
print ("estamos averiguando si este valor esta en la lista" in lista5) # nos devuelve un valor booleano = true

print ("etse elemento no esta en la lista" in lista5) # nos devuelve un valor booleano = false

