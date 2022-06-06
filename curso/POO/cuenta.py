class Cuenta ():

    def __init__(self, pro, sal, mon):
        self.__propietario = pro
        self.__saldo = sal
        self.__moneda = mon
        
    # Getters (Metodo GET)
    def get_saldo(self):
        return self.__saldo

    def get_propietario(self):
        return self.__propietario

    def get_moneda(self):
        return self.__moneda


    # Setters (Metodo SET)
    def set_moneda(self, moneda):
        self.__moneda = moneda


cuenta1 = Cuenta("oscar", 600, "soles")
print(cuenta1.get_saldo())
print(cuenta1.get_moneda())
cuenta1.set_moneda("dolares")
print(cuenta1.get_moneda())


## el get se utiliza para obtener los valores de una variable encapsulada y 
# set se utiliza para modificar los valores de una variable encapsulada.
