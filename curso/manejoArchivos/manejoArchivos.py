file = open("data1.txt", "r")

lineas = file.readlines()
print(lineas)

file.close() # cerramos el documento

######################################################################

with open( 'data2.txt', 'r') as archivo: # con esto podemos abrir el archivo y este se va a cerrar una vez que todas las lineas de codigo han sido ejecutadas dentro del with
    lineas  = archivo.readlines()
    print(lineas)
    
for l in lineas:
    print(l.replace("\n", "")) # de esta forma podemos quitar los saltos de linea
    
######################################################################

with open("data2.txt", 'r') as archivo:
    contenido = archivo.read() # lee todo el contenido del archivo
    lineas = contenido.split("\n")
    print(lineas)
    

######################################################################

with open("data2.txt", "r") as archivo:
    
    contenido = archivo.read()
    lineas = contenido.split("\n")
    pos = archivo.tell() # nos permite saber la posicion en el archivo`
    print(pos)
    print("el acrchivo tiene {0} caracteres de logitud".format(pos))
    
######################################################################

with open("data2.txt", "r") as archivo:
    
    archivo.seek(7) # nos permite movernos a una posicion en el archivo
    pos = archivo.tell()
    print(pos)
    contenido = archivo.read()
    lineas = contenido.split("\n")
    print(lineas)
    
######################################################################

with open("data2.txt", "r") as archivo:
    siguientes4 = archivo.read(7)
    print(siguientes4)
    
######################################################################

with open("data2.txt", "r") as archivo: # r - lo lee como un texto
    print(type(archivo.read()))

with open("data2.txt", "rb") as archivo: # rb - lo lee como un byte
    print(type(archivo.read()))
    

######################################################################

"""
'r' - reading mode. The default. It allows you only to read the file, not to modify it. 
When using this mode the file must exist.
'w' - writing mode. It will create a new file if it does not exist, otherwise will erase 
the file and allow you to write to it.
'a' - append mode. It will write data to the end of the file. It does not erase the file, 
and the file must exist for this mode.
'rb' - reading mode in binary. This is similar to r except that the reading is forced in 
binary mode. This is also a default choice.
'r+' - reading mode plus writing mode at the same time. This allows you to read and write 
into files at the same time without having to use r and w.
'rb+' - reading and writing mode in binary. The same as r+ except the data is in binary
'wb' - writing mode in binary. The same as w except the data is in binary.
'w+' - writing and reading mode. The exact same as r+ but if the file does not exist, 
a new one is made. Otherwise, the file is overwritten.
'wb+' - writing and reading mode in binary mode. The same as w+ but the data is in binary.
'ab' - appending in binary mode. Similar to a except that the data is in binary.
'a+' - appending and reading mode. Similar to w+ as it will create a new file if the file 
does not exist. Otherwise, the file pointer is at the end of the file if it exists.
'ab+' - appending and reading mode in binary. The same as a+ except that the data is in 
binary.
"""

with open("data3.txt", "w") as archivo:
    archivo.write("hola mundo\nestamos aprendiendo python\ny creamos este archivo para decirlo")

with open("practica.py", "w") as archivo: # de esta forma podemos crear un nuevo archivo
    archivo.write("print('hola mundo')")
