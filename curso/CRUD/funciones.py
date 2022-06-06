def compruebaDatos(opc = 1):
    
    if opc == 1 or opc == 2:
        bucle = True
        while(bucle):
            codigo = input("Ingrese el codigo del curso: ")
            if codigo.isnumeric():
                if len(codigo) > 0 and len(codigo) <= 4:
                    bucle = False
                else:
                    print("El codigo debe tener entre 1 y 4 caracteres")
            else:
                print("El codigo debe ser numerico")
                
    if opc == 1:            
        bucle1 = True
        while(bucle1):        
            nombre = input("Ingrese el nombre del curso: ").title()
            if len(nombre) > 30:
                print("El nombre debe tener menos de 30 caracteres")
            else:
                bucle1 = False
    
        bucle2 = True
        while(bucle2):
            creditos = int(input("Ingrese los creditos del curso: "))
            if len(str(creditos)) == 1:
                if creditos > 0 and creditos < 8:
                    bucle2 = False
                else:
                    print("Los creditos deben ser mayor a 0 y menor a 8")
            else:
                print("Los Creditos no pueden tener mas de un digito")
        
        #ternario = [(codigo, nombre, creditos), codigo]
        
    if opc == 1:
        curso = (codigo, nombre, creditos)
    elif opc == 2: 
        curso = codigo
        
    
    return curso

def listarCursos (cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. codigo: {1} | Nombre: {2} ({3} Creditos)".format(contador, cur[0], cur[1], cur[2])
        print(datos)
        contador+=1
    
    print(" ")

def pedirDatosRegistro():
    curso = compruebaDatos()
    return curso

def pedirDatosActualizar():
    curso = compruebaDatos()
    return curso

def pedirCodicoEliminar():
    codigo = compruebaDatos(2)
    return codigo
    