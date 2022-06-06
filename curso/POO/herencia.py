class Persona(): # clase padre 
    
    def __init__(self, apePat, apeMat, nom):
        
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombre = nom
        
    def mostrarNombreCompleto(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

    def datos(self):
        print (self.mostrarNombreCompleto())

class Estudiante(Persona): # clase hijo
            #     ^^^^^^  de esta fomar podemos herador los atributos de otra clase
    def __init__(self, apePat, apeMat, nom, pro,):
        super().__init__(apePat, apeMat, nom) # como vamos a agregar un nuevo atributo profesion en el cual no esta en la clase padre, debemos llamar al constructor de la clase padre mediante super()
        self.profesion = pro
        
    def datos(self):  # aqui estamos sobreescribiendo el metodo datos de la clase padre
        super().datos()
        print("Profesion: {0}".format(self.profesion))
    
    
estu1 = Estudiante("Torres", "Perez", "Juan", "Ingenieria civil")
per1 = Persona("Lara", "Jose", "Carlos")
# print(estu1.mostrarNombreCompleto())
# print(estu1.profesion)

# estu1.datos()

print(isinstance(estu1, Estudiante)) # verifica si un objeto es una instancia de una clase

print (isinstance(per1, Estudiante))

## herencia, podeos hacer que los atributos de una clase padre
# sean accesibles desde una clase hija de tal manera que no tengamos
# repetir codigo. pero cuando una clase hijo necesita agregar un nuevo atrivuto podemos usar Sauper()