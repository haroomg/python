# cuando indicamos un asterisco * adelante del parametro de una funcion, estamos indicanod que se va a recibir un numero indeterminado
# de parametros. ademas, esos parametros se recibiran en forma de tupla


# def devuelveLenguajes(*lenguajes):
#     for leng in lenguajes: # de esta forma podemos recorrer los datos en el yield
#         yield leng

def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        for letra in leng: # de esta forma podemos recorrer los letras uno a uno de los datos anidados en yield
            yield from leng



lenguajesObtenidos = devuelveLenguajes("python", "java", "PHP", "Ruby", "javascript")

print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))