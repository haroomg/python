# factorial: Es el producto de todos los números naturales desde 1 hasta n.

# factorial de 5: 5 * 4 * 3 * 2 * 1 = 120
# factorial de 6: 6 * 5 * 4 * 3 * 2 * 1 = 720


print (" Este sistema se encarga de de calcular el factorial de un numero")

numero = int(input("ingrese el numero que desea calcular el factorial: "))
x = 1

for i in range(1, (numero + 1)):
    x = i * x

print(" El factorial de {0} es {1}".format(numero, x))
