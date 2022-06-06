import math

numeros = [1,4,9,16,25]

# la lista interna es asignada a la variable cuando todos los elementos han sido procesados
# ejemplo de lista interna 1:
raices = [int(math.sqrt(x)) for x in numeros] # list comprehension
print(raices) 


"""

raices = []

for n in numeros:
    raices.append(int(math.sqrt(n)))  # esto equivale a list comprehension


"""

# ejemplo de lista interna 2:
v = [x if (x > 10) else "*" for x in numeros]
print(v)

# ejemplo de lista interna 3:
l = [c.upper() for c in "palabraPrueba"]
print(l)

# ejemplo de lista interna 3:

a = [l if l in "aeiou" else '*' for l in "murcielago"]
print(a)