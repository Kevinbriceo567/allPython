from tkinter import *

# VENTANA RAIZ #
raiz = Tk()

raiz.title("UNAB")  # ESTABLECER TÍTULO

#raiz.geometry("600x300") # SE AJUSTA AL TAMAÑO DEL CONTENEDOR INTERNO

raiz.config(bg="red")  # COLOR

raiz.resizable(True, True)  # PERMITIR O DENEGAR CAMBIO DE TAMAÑO

# raiz.iconbitmap("UNAB.ico")  # ICONO PERSONALIZADO

# FRAME #
myFrame = Frame()

myFrame.pack()  # METE AL FRAME DENTRO DE LA RAIZ

# myFrame.pack(fill="x")  # EXPANDE EL FRAME HORIZONTALMENTE
# myFrame.pack(fill="x", expand=True)  # EXPANDE EL FRAME TOTALMENTE
# myFrame.pack(side="right")

myFrame.config(bg="black")

myFrame.config(width="650", height="350")

myFrame.config(relief="groove")  # BORDE DEL FRAME

myFrame.config(bd=35)  # TAMAÑO DE BORDE

myFrame.config(cursor="hand2")  # CAMBIA EL CURSOR A MANO

raiz.mainloop()  # EJECUCIÓN DE LA VENTANA