# polimorfirmo  (poli => muchas / morfos: formas)

class Estudiante():
    
    def describir(self):
        print("soy un buen estudiante.")

class Docente():
    
    def describir(self):
        print("Me dedico a ensenar cursos.")    
        
class Trabajador():
    
    def describir(self):
        print("Trabajo dentro de una gran empresa.")    
        
        
def describirPersona(persona):
    persona.describir()
    
doc1 = Trabajador()
describirPersona(doc1)