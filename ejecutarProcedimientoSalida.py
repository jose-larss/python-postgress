"""
EJECUTAR PROCEDIMIENTOS ALMACENADOS CON PARÁMETROS DE SALIDA
    • Crear un procedimiento almacenado en MySQL que reciba un número de departamento como parámetro de salida, y devuelva una localidad con un parámetro de salida.
    • Realizar la llamada al procedimiento almacenado desde una aplicación Python.

"""

import psycopg2

""", port='3306'"""
bd_conexion = psycopg2.connect(host='localhost',
                                user='postgres', 
                                password='1234', 
                                database='hospital')


cursor = bd_conexion.cursor()


dp = input("Número de departamento:")
loc=""

#result_args = cursor.callproc('DevolverLocalidad', args)
result_args = cursor.execute("call devolverLocalidadFun(%s)", (dp,))
print(result_args[0])

bd_conexion.commit()

cursor.close()
bd_conexion.close()