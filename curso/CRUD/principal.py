from DB.conexion import DAO
from funciones import listarCursos, pedirDatosRegistro, pedirDatosActualizar, pedirCodicoEliminar

def menuPrincipal():
    
    continuar = True
    
    while(continuar):
        
        opcionCorrecta = False
        while (not opcionCorrecta):
            print("==== MENU PRINCIPAL ====")
            print("1. Listar cursos.")
            print("2. Agregar curso.")
            print("3. Actualizar curso.")
            print("4. Eliminar curso.")
            print("5. Salir.")
            print("======================")
            
            opcion = int(input("Ingrese una opción: "))
            
            if opcion < 1 or opcion > 5:
                print("Opción inválida , ingrse nueva mente una opcion valida.")

            elif opcion == 5:
                continuar = False
                print("Gracias por usar el sistema!!!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)
        
def ejecutarOpcion(opcion):
    dao = DAO()
    
    if opcion == 1:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                listarCursos(cursos)
            else:
                print ("No se encontraron cursos.")
        except :
            pass
        
    elif opcion == 2:
        
        curso = pedirDatosRegistro()
        
        try:
            dao.registarCurso(curso)
        except:
            print("Ocurrio un error....")
            
    elif opcion == 3:
        curso = pedirDatosActualizar()
        
        try:
            dao.actualizarCurso(curso)
        except:
            print("Ocurrio un error....")
        
    elif opcion == 4:
        curso = pedirCodicoEliminar()
        
        try: 
            dao.eliminarCurso(curso)
        except:
            print("Ocurrio un error....")
        
    else:
        print("Opción inválida")

menuPrincipal()