# las funciones lanbda son funciones anonimas, que no tienen nombre.

# def sumar (n1, n2):
#     return n1 + n2

# print(sumar(1, 2))

# toda funcion lambda se puede convertir a una funcion normal pero no viceversa

sumar = lambda n1, n2: n1 + n2 # lambda es una funcion anonima

print (sumar(1, 2))

sumar2 = sumar(55, 66)

print(sumar2)

elevarCuadrado = lambda n: n**2

print(elevarCuadrado(5))