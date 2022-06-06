# while:  es una estructura repetitiva que nos permite realizar multiples iteraciones
# hasta que la iteracion no deje de ser verdadera esta no se detendra

indice = 1

while (indice <= 10):
    print("valor actual: {0}".format(indice))
    indice +=1

print (" se ha teminado el bucle while")

inicio = 2

while (inicio <= 100):

    if ((inicio % 2) == 0):
        print(inicio)
    inicio+=1