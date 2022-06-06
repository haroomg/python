class Curso():
    #nombre =  ""
    #creditos = 0
    #profesion = ""
    #############################################
    # etsado inicial del objeto: constructor
    def  __init__(self, non, cre, pro):
        self.nombre = non
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "presencial" # propiedad encapsulada de una variables
        # podmeos acceder a la variable encapsulada dedes la clase
        
    def mostrarDatos(self):
        dat = "nombre: {0} / creditos: {1} / Modo de imparticion: {2}" 
        print(dat.format(self.nombre, self.creditos, self.__imparticion))
        docenteAsignado = self.__verificarDocente()
        
        if docenteAsignado:
            print("Existe docente asiganso")
        else:
            print("No es necesario docente asignado")
        
        
    def __verificarDocente (self): # de esta forma se puede encapsular una funcion
        #print("verificar si el docente asignado...")
        if self.__imparticion == "presencial":
            return True
        else:
            return False 
        
    # funcion toString =  __str__   
    #cunado queremos llamr la variables curso1 lo que nos dara de retorno es la direccion de memoria
    # de la memoria, pero si queremos acceder a los datos de dicha cariable
    # ex crear una funcion __str__(), en la cual estamos declarando los datos 
    # que se van a obtener al llamar la variables en este casp curso1
    
    def __str__(self):
        texto = "Nombre: {0} / Creditos: {1}"
        return texto.format(self.nombre, self.creditos)
        
    #############################################
curso1 = Curso("matematica", 5, "Ingenieria civil")
print(curso1.nombre)
curso1.mostrarDatos()
print(curso1)


print("\n")

#curso2 = Curso("lenguaje", 4, "Ingenieria industrial")
#print(curso2.nombre, curso2.creditos, curso2.profesion)
#curso2.imparticion = "virtual"