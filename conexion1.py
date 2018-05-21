import mysql.connector

#creando diccionario
dato = {
	'user':'root',
	'password':'',
	'database':'vecinos',
	'host':'127.0.0.1'
}#dicionario

conexion = mysql.connector.connect(** dato)


cursor = conexion.cursor()#crea cursor

valores = "INSERT INTO usuarios(usuario)VALUES('1234567890')"

try:
    cursor.execute(valores)
    conexion.commit()
    print("se ha insertado")
except:
    print("no se ha podido insertar")

conexion.close()
