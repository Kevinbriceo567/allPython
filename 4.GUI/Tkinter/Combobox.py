from tkinter import *
from tkinter import ttk

raiz = Tk()

raiz.title("Combobox")

raiz.geometry("400x400")

combo = ttk.Combobox(raiz, state='readonly')
combo.config(values=["Junio"])
combo.grid(row=0, column=0)

raiz.mainloop()