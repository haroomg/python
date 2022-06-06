class Pais(object):
    def __init__(self, nom, pre):
        self.nombre = nom
        self.presidente = pre
        
    def __str__(self):
        txt = "Pais: {0} - Presidente: {1}"    
        return txt.format(self.nombre, self.presidente)
    
class Ciudad():
    
    def __init__(self, nom, hab, pai):
        self.nombre = nom
        self.habitanteas = hab
        self.pais = pai
        
    def __str__(self):
        txt = "Ciudad: {0} - Habitanteas: {1} - ({2})"
        return txt.format (self.nombre, self.habitanteas, self.pais)
        

class Urbanizacion():
    def __init__(self, nom, ciu):
        self.nombre = nom
        self.ciudad = ciu 
        
    def __str__(self):
        txt = "Urbanizacion: {0} - {1}"
        return txt.format(self.nombre, self.ciudad)
        
        
pais1 = Pais("Colombia", "Juan") 
print(pais1)   

ciudad1 = Ciudad("Bogota", "5000000", pais1)
print(ciudad1)

urba1 = Urbanizacion("Los caobos del tachira", ciudad1)
print(urba1)