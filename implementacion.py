import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alle2701",
    database="implementacion"
)

class Implementacion: 

    def pregunta():
        tabla = input("que tabla desea ver? contactos, libros, peliculas")
        while tabla != "contactos" or tabla != "libros" or tabla != "peliculas":
            tabla = input("Ingrese una opcion: contactos, libros, peliculas")

    def hacer_consulta():
        cursor = cnx.cursor()


    
