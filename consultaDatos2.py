import psycopg2

""", port='3306'"""
bd_conexion = psycopg2.connect(host='localhost',
                                user='postgres', 
                                password='1234', 
                                database='hospital')
cursor = bd_conexion.cursor()
try:
    miOficio=input("Introduce Oficio Empleado:")
    consulta=("SELECT apellido,oficio,salario FROM emp where oficio=%s")
    cursor.execute(consulta,(miOficio,))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable
    resultado=False
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
