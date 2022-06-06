# funcion: conjunto de instrucciones que realizan un proceso
# su ventaja es que ayuda a evitar repetir codigo

# funciones sin parametros
def saludar():
    print("hola mundo")

saludar()


# funciones con parametros
def evaluaSueldo(sueldo):
    if sueldo > 1000:
        print("el sueldo es mayor a 1000")
    else:
        print("ganas un sueldo minimo")

evaluaSueldo(1200)