import mysql.connector
con = mysql.connector.connect(user="root",password="",host="root",database="vecinos")
cursor=con.cursor()
cursor.execute("CREATE TABLE example (id INT, data VARCHAR(100));")
con.close()
