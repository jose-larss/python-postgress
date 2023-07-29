"""
EJECUTAR PROCEDIMIENTOS ALMACENADOS
    • Insertar registros en la tabla DEPT a través de procedimientos almacenados.
    • Pasar los tres parámetros al procedimiento almacenado.
"""


import psycopg2

""", port='3306'"""
bd_conexion = psycopg2.connect(host='localhost',
                                user='postgres', 
                                password='1234', 
                                database='hospital')

cursor = bd_conexion.cursor()

dp = input("Número de departamento:")
nombre= input("Nombre departamento:")
localidad= input("localidad:")

cursor.execute("call insertardept(%s, %s, %s)", (dp,nombre,localidad))

if cursor.rowcount>0:
    print ("Registro insertado satisfactoriamente")
else:
    print ("Dato no encontrado")

bd_conexion.commit()

cursor.close()
bd_conexion.close()