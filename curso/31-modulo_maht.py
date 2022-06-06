import math

# round - redondea un valor bien sea para arriba o para abajo, si es de 0.5 arriba y si es de 0.4 abajo
x = 1.553
print(round(x))
print(round(x, 1)) # redondea a un digito decimal
print(math.ceil(x)) # siempre va a redondear para arriba
print(math.floor(x)) # siempre va a redondear para abajo


print(math.trunc(x)) # devuelve el entero de un numero

numeros = [1,2,3,4,5,6,7,8,9,10]
print(int(math.fsum(numeros))) # suma todos los elementos de una lista


print(math.fabs(-1.553)) # devuelve el valor absoluto de un numero

print(math.fmod(17,6)) # devuelve el resto de una division

print(math.exp(2)) # epsilon - e elevado a un numero

print(math.pi) # devuelve el valor de pi

print(math.pow(5, 6)) # eleva un numero a un exponente
print(math.sqrt(16)) # raiz cuadrada

h = math.hypot(1.5, 1.5) # devuelve la hipotenusa de un triangulo rectangulo
print(h)

r = math.radians(45) # convierte un angulo en grados a radianes
print("El valor en radianes es: ", r)

print(math.sin(67)) # seno de un angulo
print(math.sin(math.radians(30))) # seno de un angulo
print(math.cos(67)) # coseno de un angulo

print(math.remainder(16, 3)) # devuelve el resto de una division