from random import randint
from numpy import Infinity 

palabras = [
    ["sal", "sol", "sol", "ato", "hoy", "ida", "ojo", "oro", "ola", "tio"],
    ["hora", "cama", "casa", "pera", "mama", "bala", "caer", "domo", "dona", "hielo"],
    ["alias", "arder", "atojo", "azote", "barrer", "lista", "china", "cofre", "blusa", "aries"],
    ["abuela", "animal", "barril", "bailar", "angulo", "biblia", "cabina", "billar", "bordes", "bocina"],
    ["acierto", "adoptar", "aflojar", "agendar", "ajustes", "alcalde", "arbitro", "bolivar", "amarres", "armario"],
    ["abduzcan", "abejones", "aciertos", "acolitos", "adefecio", "adivinar", "adultero", "afectado", "balances", "bancario"],
    ["cachalote", "abrazotes", "academias", "aflojarse", "algoritmo", "argentina", "atributos", "asiaticos", "australia", "boliviano"],
    ["aborigenes", "afganistan", "aleatorios", "alquimicos", "americanos", "abecedario", "anacoretas", "balleneras", "boligrafos", "bolchevique"]
]

posicionesDificultad  = [[0,1],[2,3],[4,5],[6,7]]

figura = ['''
   +---+
   |   |
       |
       |
       |
       |
  =========''',

'''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', 

'''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''',

'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', 

'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', 

'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', 

'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
  ========='''
  
]

def procesaPalabra(nivel, dificultad, figura):
    
    # nos da valores posiciones aleatorias de la lista de posiciones
    indiceExterno = randint(nivel[0], nivel[1])
    indiceInterno = randint(0, len(palabras[0]) -1 )
    
    # escoge una palabra de la lista de palabras
    palabra = palabras[indiceExterno][indiceInterno]
    ocultaPalabra = " _ " * len(palabra)
    intentos = dificultad
    contadorFigura = 0
    
    x =True
    
    while x:
        
        print("\n",ocultaPalabra,"\n")
        print(figura[contadorFigura])
        pregunta = input("\ningresa una letra: ").lower()
        
        if pregunta in palabra:
            for i in range(len(palabra)):
                if palabra[i] == pregunta:
                    ocultaPalabra = ocultaPalabra[:i*3] + pregunta + ocultaPalabra[i*3+1:]
            print("correcto")
            abe = ocultaPalabra.replace("_", " ")
            abe2 = abe.replace(" ", "")
            
            if abe2 == palabra:
                print("\n", ocultaPalabra, "\n")
                print("\n", "Siguiente Nivel")
                x = False
                
                return True
        else:
            intentos -= 1
            contadorFigura += 1
            if contadorFigura == 6:
                contadorFigura = 0
            print(" Intenta de nuevo.")
            if intentos == 0:
                print(figura[6])
                print("\n", "Perdiste")
                break
            
            
            

print("\n","Bienvenido al juego del ahorcado","\n")

while True:
    
    dificultad = int(input("Elija un nivel de dificultad:\n(1) Facil: Intentos infinitos.\n(2) Medio: 12 intentos.\n(3) Difficil: 6 intentos.\nRespuesta: "))
    if dificultad == 1:
        dificultad = Infinity
        break
    elif dificultad == 2:
        dificultad = 12
        break
    elif dificultad == 3:
        dificultad = 6
        break
    else:
        print("\n","Elija un nivel de dificultad valido","\n")


print(" Nivel 1: Facil.")

if procesaPalabra(posicionesDificultad[0], dificultad, figura):
    print(" Nivel 2: normal.")
    if procesaPalabra(posicionesDificultad[1], dificultad, figura):
        print(" Nivel 3: Dificil.")
        if procesaPalabra(posicionesDificultad[2], dificultad, figura):
            print(" Nivel 4: Imposible.")
            if procesaPalabra(posicionesDificultad[3], dificultad, figura):
                print("\n", "FIN DEL JUEGO")
                
                

