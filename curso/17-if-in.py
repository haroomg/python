print ("-- cursos --")
print ("Matematica - biologia - lenguaje - ciencias")

curso = str(input("ingrese el curso deseado "))

if curso in ("matematica", "biologia", "lenguaje", "ciencias"):
    print ("{0}:  curso seleccionado".format(curso))
else:
    print ("no existe este curso....".format(curso))

"""
de esta forma se puede comprobar si un valor esta en una tupla mediante if
"""