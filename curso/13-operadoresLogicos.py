# and - se tinen que cumplir todas las condiciones para que sea verdadero
# or - se tiene que cumplir una de las condiciones para que sea verdadero
# not - si una condicion es true, not lo cambia a false, si es false, lo cambia a true

distancia = 400
numeroHermanos = 3
saliarioPadres = 3000
tienenBeneficio = False 

if (((distancia > 1000) and (numeroHermanos > 2)) or (saliarioPadres < 2000)):
    tienenBeneficio = True

    if (tienenBeneficio):
        print("tienen beneficio")
else:
    print("no tienen beneficio")

print(not tienenBeneficio)

# oter example