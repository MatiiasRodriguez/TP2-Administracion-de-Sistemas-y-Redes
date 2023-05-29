import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="alle2701",
    database="implementacion"
)

def hacer_consulta(tabla):
    cursor = cnx.cursor()
    query = f"SELECT * FROM {tabla}"
    cursor.execute(query)
    resultado = cursor.fetchall()
    cursor.close()
    mostrar_consulta(resultado)

def mostrar_consulta(resultado):
    print(resultado)



        


tabla = input("que tabla desea ver? contactos, libros, peliculas: ")
if tabla == "contactos" or tabla == "libros" or tabla == "peliculas":
    hacer_consulta(tabla)
else:
    tabla = input("Ingrese una opcion: contactos, libros, peliculas: ")
