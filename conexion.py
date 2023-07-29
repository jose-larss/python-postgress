import psycopg2

def conexion_BBDD(consulta, parametros = ()):
    with psycopg2.connect(
            database="hospital", 
            user="postgres", 
            password="1234"
        ) as conexion:
        cursor = conexion.cursor()
        cursor.execute(consulta, parametros)
        resultado = cursor.fetchall()
        #conexion.commit()
    return resultado