# excepcion:  error en un tiempo de ejecucion (durate la ejecucion de un programa algo asi como un tey catch)

from typing import final


numero = 20
numero2 = 2

try:
    print ("la division entre {0} entre {1} es: {2}".format(numero, numero2, (numero/numero2)))
#except:
except ZeroDivisionError:
    print ("no se puede dividir entre cero....")

finally: # lo que este dentro de finally siempre se ejecutara
    print ("se ha terminado la ejecucion del programa") 


print ("aqui termina el programa")

"""
al momento de correr un programa y ver si este corre o no, hay una linea de codigo que no funcione,
por ejemplo podemos poner esa linea de codigo en un try y si esta faya que devualva un mensaje 
por medio del except
"""