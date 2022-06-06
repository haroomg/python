# Diccionarios: son estructuras de datos propias que permite almacenar distintos tipos de datos.

# es paracido a los objetos en javascript

# los datos se almacenan asociados a una clave unica, tenemos una relacion entre la clave y el valor

# los elementos almacenados estan desordenados, no se puede acceder a un elemento por su posicion

diccionario = {
    "españa": "madrid",
    "francia": "paris",
    "italia": "roma",
    "portugal": "lisboa"
}

print(diccionario)
# para acceder a un elemento de un diccionario
print(diccionario["españa"])

# para agregar un elemento al diccionario
diccionario["venezuela"] = "caracas"
print(diccionario)

# para modificar un elemento del diccionario
diccionario["italia"] = "new york"
print(diccionario)

# para eleminar un elemento del diccionario
del diccionario["italia"]
print(diccionario)

# tambien posemos crear una tupla o  un array y asignar un valor a cada uno de sus elementos desde el diccionario

paises = ("españa", "francia", "italia", "portugal")

capitales = {
    paises[0]: "madrid",
    paises[1]: "paris",
    paises[2]: "roma",
    paises[3]: "lisboa"
}

print(capitales)

# podemos anidar un diccionario dentro de otro diccionario

datosPersonales = {
    "nombre": "juan",
    "apellido": "perez",
    "edad": 25,
    "direccion": {
        "calle": "calle falsa",
        "numero": "123"
    }
}

# para acceder a un elemento del diccionario por ejemplo calle
print(datosPersonales["direccion"]["calle"])

# get - podemos usar la funcion get para obtener un valor de un diccionario y si este no aparece nos devuelve un valor por defecto 
print (datosPersonales.get("apellidos", "no existe"))
print (datosPersonales.get("apellido", "no existe"))

# keys - podemos usar la funcion keys para obtener una lista con las llaves de un diccionario
print(datosPersonales.keys())

# values - tambien podemos acceder a los valores de un diccionario con la funcion values
print (datosPersonales.values())

# tambien podemos tranformar un diccionario en una lista o tupla

valores = list(datosPersonales.values())
print(valores)

valores = tuple(datosPersonales.values())
print(valores)