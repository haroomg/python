# Map: Aplica una funcion a cada elemento de una lista iterable, devlviendo otra lista

def elevarCuadrado(nun):
    # return nun ** nun
    return pow (nun, 2)

# numeros = [1,2,3,4,5,6,7,8,9,10]   

numeros = list(range(1,11)) 
print(numeros)

numerosElevados = list(map(elevarCuadrado, numeros))

print(numerosElevados)