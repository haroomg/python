"""
de esta forma se puede hacer una comparacion de dos variables

tring sexo;
sexo = (10 > 2) ? "masculino" : "femenino";

pero en python no se puede hacer de esta forma
"""

sexos = ("hombre", "mujer")

posicion = True
sexo = sexos[posicion]
print(sexo)
sexo = sexos[not posicion]
print(sexo)

# ya que true quevale a 1 y false a 0, se puede hacer de esta forma para accrder a la posicion de la tupla