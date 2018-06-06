import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTOS (NOBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miConexion.commit()
miConexion.close()
