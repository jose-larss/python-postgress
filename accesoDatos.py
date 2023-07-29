"""
    • import mysql.connector as bd

Importamos el connector para poder utilizar las funciones presentes en la librería.

    • bd.connect
	
Con la función connect nos conectamos a MYSQL, indicando el servidor, puerto, usuario, contraseña y base de datos.

    • bd_conexion.cursor()

Creamos un cursor para almacenar los datos devueltos por la consulta.

    • cursor.execute("SELECT apellido,oficio,salario FROM emp")

La función o método execute permite ejecutar una consulta SQL.



    • for ape, ofi, sal in cursor:
        print("Apellido: " + ape)
        print("Oficio: " + ofi)
        print("Salario: " + str(sal))

Recorremos los datos del cursor para ir imprimiendo los valores.	

    • bd_conexion.close()

Por último, cerramos la conexión a la base de datos.
(También podríamos cerrar el cursor)
"""
import psycopg2

"""Estos parametros correctos para mysql"""
bd_conexion = psycopg2.connect(user='postgres', password='1234', database='hospital')
cursor = bd_conexion.cursor()
try:
    cursor.execute("SELECT apellido,oficio,salario FROM emp")

    for ape, ofi, sal in cursor:
        print("Apellido: " + ape)
        print("Oficio: " + ofi)
        print("Salario: " + str(sal))

except bd_conexion.Error as error:
    print("Error: ",error)

cursor.close()
bd_conexion.close()