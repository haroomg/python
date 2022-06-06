from colorama import Cursor
import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "",
                db = "prueba_db"
            )
        
        except Error as ex:
            print("Error: {0}".format(ex))
        
    # listar cursos de la base de datos
    def listarCursos(self):
        if self.conexion.is_connected():    
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY codigo ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error: {0}".format(ex))
        else:
            print("Error en listar cursos.")
    
    # insertar curso a la base de datos
    def registarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', {2})".format(curso[0], curso[1], curso[2])
                cursor.execute(sql)
                self.conexion.commit()
                print("Curso registrado con exito.\n")
            except Error as ex:
                print("Error: {0}".format(ex))
        else:
            print("Error en crear curso.")
            
    # actualizar curso de la base de datos        
    def actualizarCurso (self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET nombre = '{0}', creditos = '{1}' WHERE codigo = '{2}'".format(curso[1], curso[2], curso[0])
                cursor.execute(sql)
                self.conexion.commit()
                print("Curso Actualizado con exito:")
                print(" {0}  {1}  {2} \n".format(curso[0], curso[1], curso[2]))
            except Error as ex:
                print ("Error: {0}".format(ex))
        else:
            print("Error en actualizar curso.")
            
    # eliminar curso de la base de datos
    def eliminarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE codigo = '{0}'".format(curso)
                cursor.execute(sql)
                self.conexion.commit()
                print("Curso eliminado con exito.\n")
            except Error as ex:
                print("Error: {0}".format(ex))
        else:
            print("Error en eliminar curso.")
        