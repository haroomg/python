import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        port = 3306,
        user = "root",
        password = "",
        db = "prueba_db"
        
    )
    
    if conexion.is_connected():
        # print("Conexion establecida")
        cursor = conexion.cursor()
        cursor.execute("SELECT database();")
        registro = cursor.fetchone() # fetch = - es un objeto que nos devuelve algo de la base de datos - fetchone = devuelve un registro de la base de datos
        # print("Base de datos seleccionada: {0}".format(registro)) 
        
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall() # fechtall - devulve todos los registro de la base de datos
        for fila in resultados:
            print(fila[0], "-", fila[1], fila[3])
            
        print("total de registros: ", cursor.rowcount)
        
except Error as ex:
    print("Error: {0}".format(ex))
    
finally:
    if conexion.is_connected():
        conexion.close() # se cerro la conexion a la base de datos
        print("Conexion cerrada")