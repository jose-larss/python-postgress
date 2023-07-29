"""
    • Desarrollar una aplicación que nos pida por teclado un oficio de un empleado.
    • Mostrar en pantalla el apellido, oficio y salario de los empleados que coincidan con el dato introducido.
"""
import psycopg2

from conexion import conexion_BBDD

"""port='3306',"""

"""
bd_conexion = psycopg2.connect(host='localhost', 
                                   user='postgres', password='1234', database='hospital')
cursor = bd_conexion.cursor()
try:
    miOficio=input("Introduce Oficio Empleado:")
    consulta=("SELECT apellido,oficio,salario FROM emp where oficio=%s")
    cursor.execute(consulta,(miOficio,))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable

    for ape, ofi, sal in cursor:
         print("Apellido: ", ape)
         print("Oficio: " ,ofi)
         print("Salario: " , str(sal))

except bd_conexion.Error as error:
    print("Error: ",error)

cursor.close()
bd_conexion.close()

"""

miOficio=input("Introduce Oficio Empleado:")
consulta=("SELECT * FROM emp where oficio=%s")
persona = conexion_BBDD(consulta, (miOficio,))

# Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable

if len(persona) > 0:
    for item in persona:
        print(item)
else:
    print(f'No ha personas con el oficio {miOficio}')


