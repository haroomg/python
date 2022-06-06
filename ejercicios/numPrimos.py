print ("mediante este sistema podemos saber si un numero es primo")

numPrimo = int (input("ingrese el numero que desea saber si es primo: "))
contador = 0

for i in range (1, (numPrimo + 1)):
    if (numPrimo % i) == 0:
        contador+=1
        
if (contador == 2):
    print("El numero {0} es primo".format(numPrimo))
else: 
    print("\nEl numero {0} no es primo".format(numPrimo))