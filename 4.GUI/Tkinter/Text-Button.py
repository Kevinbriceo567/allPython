from tkinter import *

# ROOT
root = Tk()

root.geometry("500x500")

# FRAME
frame = Frame(root)

frame.config(width="500", height="500")

frame.pack()

myName = StringVar()  # TEXTO A MOSTRAR EN BOTON ENVIAR

# ENTRY NOMBRE
entradaN = Entry(frame, textvariable=myName)  # CUADRO DE TEXTO

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

# ENTRY WRITE
file = open("sampleText.txt", "r")
writeT = Text(frame, width=20, height=5)
writeT.insert(INSERT, "")  # INSERTAR TEXTO AL CUADRO
writeT.grid(row=2, column=1)

# SCROLLBAR
barraV = Scrollbar(frame, command=writeT.yview)
barraV.grid(row=2, column=2, sticky="nsew")
writeT.config(yscrollcommand=barraV.set)  # AHORA LA BARRA INDICA POSICIÓN ESPECÍFICA

# LABEL TXT
writeL = Label(frame, text="Escribe:")
writeL.grid(row=2, column=0, sticky="e")
writeL.config(padx=10, pady=10)

def codigoBoton():
    myName.set("Kevin")

# BUTTON
boton = Button(root, text="Enviar", command=codigoBoton)
boton.pack()

root.mainloop()