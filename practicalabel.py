from tkinter import *
root=Tk()
root.title("Ventana de Prueba")
root.config(bg="blue")
miframe=Frame(root, width=500, height=400)
miframe.pack(side="left", anchor="n")

Label(miframe,text="Hola alumnos de python", fg="red", font=("Comic Sans MS", 18)).place(x=100,y=200)
#miframe.pack()
miimagen=PhotoImage(file="Graficos/raton.png")
Label(miframe, image=miimagen).place(x=100, y=250)


root.mainloop()