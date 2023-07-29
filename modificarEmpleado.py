"""
MODIFICANDO REGISTROS EN BASE DE DATOS
    • Realizar una aplicación que nos permita modificar registros de la base de datos.
    • Modificaremos el salario de un determinado empleado. 
    • Solicitar el nuevo salario y el número del empleado a modificar.
"""
import psycopg2

""", port='3306'"""
bd_conexion = psycopg2.connect(host='localhost',
                                user='postgres', 
                                password='1234', 
                                database='hospital')

cursor = bd_conexion.cursor()

ConsultaModificacion = ("Update emp set salario=%s where emp_no=%s")

NumeroEmpleado = input("Número de empleado a modificar:")
NuevoSal= input("Nuevo salario:")

cursor.execute(ConsultaModificacion, (NuevoSal,NumeroEmpleado,))
if cursor.rowcount>0:
    print ("Registro modificado satisfactoriamente")
else:
    print ("Dato no encontrado")

bd_conexion.commit()

cursor.close()
bd_conexion.close()
