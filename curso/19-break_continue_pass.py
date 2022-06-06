# Break: permite salir de un bucle o iteracion cuando se cumple una condicion

for numero in range(1,6):
    if numero == 3:
        print("se ha encontrado el numero 3")
        break # se detiene la ejecucion del bucle
    print("el numero es: {0}".format(numero))

print("fin del programa")



# Continue: permite continuar con la siguiente iteracion sin terminar la actual si se cumple una condicion

for numero in range(1,6):
    if numero == 3:
        print("se ha encontrado el numero 3")
        continue # se detiene la ejecucion de la iteracion actual y continua con la siguiente
    print("el numero es: {0}".format(numero))

print("fin del programa")



# pass: permite continuar con una sentencia o funcion que ya no tiene o aun no tiene un bloque de codigo util
for numero in range(1,6):
    if numero <= 3:
        # aqui no pasa nada y el bucle continua
        pass 
    else:
        print("el siguiente numero es mayor a 3")
    print("el numero es: {0}".format(numero))

print("fin del programa")

# tambien podemos usar pass en una funcion que todavia no tiene codigo

def funcionSinImplementar():
    pass