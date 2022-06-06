# concatenacion de variables

texto1 = "Hola"
texto2 = "Mundo"

# 1. Concatenacion
texto3 = texto1 + " " + texto2
print(texto3)

# 2. Concatenacion con %s %(variable)
print ("El saludo es: %s %s" % (texto1, texto2))

# 3. Concatenacion con format
saludoFinal = "saludo: {0} {1}".format(texto1 , texto2)
print(saludoFinal)

# 4. Concatenacion con format
saludoFinal2 = "saludo: {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal2)