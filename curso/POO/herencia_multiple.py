class CalseA ():
    
    def __init__(self, par1, par2):
        self.parametro1 = par1
        self.parametro2 = par2
        
class CalseB ():
    def __init__(self, par3, par4 , par5):
        self.parametro3 = par3
        self.parametro4 = par4
        self.parametro5 = par5

class ClassX (CalseA, CalseB):
    pass

cx1 = ClassX(14, 21)

# una clase hijo puede heredar de varias clases padres