from io import open

archivo_texto=open("archivo.txt","w")

frase="EStupendo dia para estudiar Python \n el Miercoles"
archivo_texto.write(frase)

archivo_texto.close()

from io import open

archivo_texto=open("archivo.txt","r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)



from io import open

archivo_texto=open("archivo.txt","r")

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto)


from io import open

archivo_texto=open("archivo.txt","r")

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[0])

print(lineas_texto[1])


from io import open

archivo_texto=open("archivo.txt","a")

frase="\n Siempre es bueno estudiar Python"
archivo_texto.write(frase)

archivo_texto.close()