texto_minuscula = "bienvenidos al imalaya"

texto_mayuscula = "BIENVENIDOS AL IMALAYA"

print(texto_minuscula.upper()) # convertir las minusculas a mayuscula
print(texto_mayuscula.lower()) # convertir las mayusculas a minusculas
print(texto_minuscula.title()) # convertir la primera letra de cada palabra a mayuscula
print (texto_minuscula.find("al")) # buscar la palabra al en el texto y regresa su posicion en la lista
print(texto_minuscula.count("a")) # nos muestra cuantas veces se repite un elemento en el string

reemplazar = texto_minuscula.replace("al", "AL") # reemplaza un elemento por otro
print(reemplazar) 

valor = texto_minuscula.isnumeric() # nos dice si el string es numerico con true o false
print(valor)

cadenaSeparada = texto_minuscula.split(" ") # separa un string en una lista
print(cadenaSeparada)