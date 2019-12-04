from tkinter import *

# ROOT
root = Tk()

root.geometry("500x500")

# FRAME
frame = Frame(root)

frame.config(width="500", height="500")

frame.pack()

# ENTRY NOMBRE
entradaN = Entry(frame)  # CUADRO DE TEXTO

entradaN.grid(row=0, column=1)  # USANDO GRID

# LABEL NOMBRE
nameL = Label(frame, text="Nombre:")
nameL.grid(row=0, column=0, sticky="e")  # MANTENER TEXTO PEGADO AL CUADRO
nameL.config(padx=10, pady=10)  # MARGEN CON CONTENEDOR

# ENTRY APELLIDO
entradaA = Entry(frame)  # CUADRO DE TEXTO

entradaA.grid(row=1, column=1)

# LABEL APELLIDO
lastL = Label(frame, text="Apellido:")
lastL.grid(row=1, column=0, sticky="e")
lastL.config(padx=10, pady=10)

# ENTRY PASS (CONTRASEÑA)
entradaP = Entry(frame)  # CUADRO DE TEXTO

entradaP.config(show="*")

entradaP.grid(row=2, column=1)

# LABEL PASS
passL = Label(frame, text="Contraseña:")
passL.grid(row=2, column=0, sticky="e")
passL.config(padx=10, pady=10)

root.mainloop()
