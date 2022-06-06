# Raise = sirve para lanzar ( de forma intencional ) excepciones en python

def evaluarNota (nota):
    if nota < 0:
        raise ValueError ("valor incorrectp...")
        # raise ZeroDivisionError ("no se permite valores negativos")
    elif nota >= 16:
        print("excelente")
    elif nota >+ 11:
        print ("aprobado")
    else:
        print("desaprobado")
        

evaluarNota(-6)
print("fin del programa")