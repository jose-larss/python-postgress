"""
ELIMINANDO REGISTROS EN BASE DE DATOS
    • Solicitar un número de empleado por teclado y almacenarlo en una variable.
    • Borrar el empleado cuyo número de emp coincida con el introducido.
"""

import psycopg2

""", port='3306'"""
bd_conexion = psycopg2.connect(host='localhost',
                                user='postgres', 
                                password='1234', 
                                database='hospital')


cursor = bd_conexion.cursor()

ConsultaBaja = ("Delete from emp where emp_no=%s")

NumeroEmpleado = input("Número de empleado a eliminar:")

cursor.execute(ConsultaBaja, (NumeroEmpleado,))
if cursor.rowcount>0:
    print ("Registro eliminado satisfactoriamente")
else:
    print ("Dato no encontrado")

bd_conexion.commit()

cursor.close()
bd_conexion.close()