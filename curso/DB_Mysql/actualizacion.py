import mysql.connector
from mysql.connector import Error

# funciones que validan la integridad de los datos

def validaPrimerNombre():
    nom1 = input("Ingrese su primer nombre: ").title()
    
    if len(nom1) >= 3 and len(nom1) <= 20:
        return nom1
    
    else:
        print("ingreso los datos mal, intente de nuevo")
        validaPrimerNombre()

def validaSegundoNombre():
    nom2 = input("Ingrese su segundo nombre: ").title()
    
    if len(nom2) >= 3 and len(nom2) <= 20:
        return nom2
    else:
        print("ingreso los datos mal, intente de nuevo")
        validaSegundoNombre()
    
def validaPrimerApellido():
    ape1 = input("Ingrese su primer apellido: ").title()
    if len(ape1) >= 3 and len(ape1) <= 20:
        return ape1
    else:
        print("ingreso los datos mal, intente de nuevo")
        validaPrimerApellido()
    
def validaSegundoApellido():
    ape2 = input("Ingrese su segundo apellido: ").title()
    
    if len(ape2) >= 3 and len(ape2) <= 20:
        return ape2
    else:
        print("ingreso los datos mal, intente de nuevo")
        validaSegundoApellido()
    
def validaTelefono():
    tel = input("Ingrese su numero de telefono: ")
    if len(tel) >= 10 and len(tel) <= 15:
        if tel.isnumeric():
            tel = str(tel)
            return tel
        else:
            print("ingreso los datos mal, intente de nuevo")
            validaTelefono()
    else:
        print("ingreso los datos mal, intente de nuevo")
        validaTelefono()
    
def validaEmail():
    correo = input("Ingrese su correo electronico: ")
    if len(correo) >= 10 and len(correo) <= 100:
        return correo
    else:
        print("ingreso los datos mal, intente de nuevo")
        validaEmail()

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        password = "",
        db = "prueba_db"
        
    )
    
    if conexion.is_connected():
        print("Conexion establecida")
        cursor = conexion.cursor()
        
        id = int(input("Ingrese el ID de los datos de la persona que sea modificar: "))
        
        nom1 = validaPrimerNombre()
        
        nom2 = validaSegundoNombre()
        
        ape1 =validaPrimerApellido()
        
        ape2 = validaSegundoApellido()
        
        tel = validaTelefono()
        
        correo = validaEmail()

        cursor.execute("""UPDATE usuarios SET primer_nombre = '{0}', segundo_nombre = '{1}',
                        primer_apellido = '{2}', segundo_apellido = '{3}', num_telefono = '{4}', email = '{5}'
                        WHERE id_user = {6}""".format(nom1, nom2, ape1, ape2, tel, correo, id))
        
        conexion.commit() # commit = confirma la conexion que estamos ejecutando
        print(" {0}  {1}  {2}  {3}  {4}  {5} ".format(nom1, nom2, ape1, ape2, tel, correo))
        
except Error as ex:
    print("Error: {0}".format(ex))
    
finally:
    if conexion.is_connected():
        conexion.close() # se cerro la conexion a la base de datos
        print("Conexion cerrada")
        
