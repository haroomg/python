"""

En que consite la programacion orientada a objetos?

- En trasladar la naturaleza de los objetos de la vida real a codigo 
de programcion (en algun lenguaje de programacion).

los objetos de la realidad tienen caracteristicas (atributos o propiedades) y funcionalidades o comportamiento (fuciones o metodos).

ventajas:
- Modularizacion (division en pequeños partes) de un programa complejo.
- Codigo funete muy reutilizable.
- codigo fuente mas facil de incementar en el futuro y mantener.
- si existe un fallo en una pequeña parte del codigo el programa completo no 
debe fallar necesariamente. Ademas, es mas facil de corregir esos fallos.
- Encapsulamiento: Ocultamineto del funcionamineto interno de un objeto.

"""

###############################################################################
class  Persona():
    #propiedades, Caracteristicas p otributos
    apellido = ""
    nombre = ""
    edad = 0
    despierta = False
    
    # funcionalidades
    
    def despertar (self):
        # self: parametro  que hace referencia a la insatcia perteneciennte a la clase.
        self.despierta = True # con self, tenemos acceso a las variables de la clase persona.
        print("buen dia.")
        
    def dormir (self):
        self.despierta = False
        print ("buenas noches")
###############################################################################

persona1 = Persona()
persona1.apellido = "Garcia funete"
print (persona1.apellido)
persona1.despertar()
print(persona1.despierta)

print("\n")

persona2 = Persona()
persona2.apellido = "Perez Reverte"
print(persona2.apellido)
persona2.dormir()
print(persona2.despierta)