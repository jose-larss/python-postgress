"""
CONSULTAS CON VARIOS PARÁMETROS
    • Crear una aplicación que nos solicite por teclado dos valores correspondientes a salarios de los empleados
    • Visualizar en pantalla los empleados que tengan un salario entre los dos valores introducidos.
"""

import psycopg2

""", port='3306'"""
bd_conexion = psycopg2.connect(host='localhost',
                                user='postgres', 
                                password='1234', 
                                database='hospital')
cursor = bd_conexion.cursor()
try:
    print ("Introduzca rango Salarial\n")
    v1=input("Valor 1:")
    v2 = input("Valor 2:")
    consulta=("SELECT apellido,oficio,salario FROM emp where salario > %s and salario < %s")
    #consulta=("SELECT apellido,oficio,salario FROM emp where salario between %s and %s")
    cursor.execute(consulta,(v1,v2))

    resultado=False
    print ("\n")
    for ape, ofi, sal in cursor:
         print("Apellido: ", ape)
         print("Oficio: " ,ofi)
         print("Salario: " , str(sal))
         resultado=True
    if resultado==False:
       print ("Sin resultados")

except bd_conexion.Error as error:
    print("Error: ",error)

cursor.close()
bd_conexion.close()