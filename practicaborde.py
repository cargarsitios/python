from tkinter import *
root=Tk()
root.title("Ventana de Prueba")
root.config(bg="blue")
#root.resizable(True,False)
#root.geometry("650x350")
root.config(bd=45)
root.config(relief="groove")
root.config(cursor="hand2")

miframe=Frame()
miframe.pack()
miframe.config(bg="red")
miframe.config(width="650", height="350")
miframe.config(bd=35)
#miframe.config(relief="groove")
miframe.config(relief="sunken")
miframe.config(cursor="pirate")
root.mainloop()