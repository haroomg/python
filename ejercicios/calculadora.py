bucleFin = True

while(bucleFin):
    
    num1 = int(input("\ningrese un valor: "))
    num2 = int(input("\ningrese un segundo valor: "))
    ope = input("\nElija la operacion matematica deceada: \n 1- suma.\n 2- resta.\n 3- multiplicacion.\n 4- division.\nRespuesta: ")
        
    if ((ope == "1") or (ope == "suma" )or (ope == "Suma") or (ope == "SUMA") or( ope == "+")):
        print ("{0} + {1} = {2}".format(num1, num2, (num1 + num2)))
        
    elif(ope == "2" or ope == "resta" or ope == "Resta" or ope == "RESTA" or ope == "-"):
        print ("{0} - {1} = {2}".format(num1, num2, (num1 - num2)))
        
    elif(ope == "3" or ope == "multiplicacion" or ope == "Multiplicacion" or ope == "MULTIPLICACION" or ope == "*"):
        print("{0} * {1} = {2}".format(num1, num2, (num1 * num2)))
        
    elif(ope == "4" or ope == "division" or ope == "Division" or ope == "DIVISION" or ope == "/"):
        print("{0} / {1} = {2}".format(num1, num2, (num1 / num2)))
    else:
        print("\nOperacion no valida (Se ingrso un valor mayor a 4 y menor a 1 o una de los o esta mal escrita la peticion)")
        
    prefuntaFinBucle = input("\nDesea realizar otra operacion? (si/no): ")
    
    if ((prefuntaFinBucle == "no") or (prefuntaFinBucle == "No") or (prefuntaFinBucle == "NO")):
        bucleFin = False