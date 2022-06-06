from http.client import NON_AUTHORITATIVE_INFORMATION


# al sumar dos nuemros que estan pasado como strings estos no de van a sumar sino que se van a concadenar
nun1 = '5'
nun2 = '10'
print(nun1 + nun2)

# los los strings que tenemos los estamos pasando a numeros
numero1 = int(nun1)
numer2 = int(nun2)
print(numero1 + numer2)

# los numeros que tenemos los volvemos a pasar a strings
numbre1 = str(numero1)
numbre2 = str(numer2)
print(numbre1 + numbre2)

# len - la funcion len nos puede decir la longitud de un string
phoneNumber = 123456789
print(len (str(phoneNumber)))