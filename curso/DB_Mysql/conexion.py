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
        print("Conexion establecida")
        infoCerver = conexion.get_server_info()
        print("Informacion del servidor: ", infoCerver)
        
except Error as ex:
    print("Error: {0}".format(ex))
    
finally:
    if conexion.is_connected():
        conexion.close() # se cerro la conexion a la base de datos
        print("Conexion cerrada")